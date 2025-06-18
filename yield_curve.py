import QuantLib as ql

def build_yield_curve():
    today = ql.Date.todaysDate()
    ql.Settings.instance().evaluationDate = today

    calendar = ql.TARGET()

    # Short-term instruments: Deposits
    deposit_rates = [(1, ql.Weeks, 0.0015), (1, ql.Months, 0.002)]
    deposit_helpers = [
        ql.DepositRateHelper(
            ql.QuoteHandle(ql.SimpleQuote(rate)),
            ql.Period(length, unit),
            2,
            calendar,
            ql.ModifiedFollowing,
            False,
            ql.Actual360()
        )
        for length, unit, rate in deposit_rates
    ]

    # Long-term instruments: Swaps
    swap_rates = [(2, ql.Years, 0.005), (5, ql.Years, 0.01), (10, ql.Years, 0.015)]
    swap_helpers = [
        ql.SwapRateHelper(
            ql.QuoteHandle(ql.SimpleQuote(rate)),
            ql.Period(length, unit),
            calendar,
            ql.Annual,
            ql.Unadjusted,
            ql.Thirty360(ql.Thirty360.BondBasis),
            ql.Euribor6M()
        )
        for length, unit, rate in swap_rates
    ]

    # Combine all helpers
    rate_helpers = deposit_helpers + swap_helpers

    yield_curve = ql.PiecewiseLinearZero(
        today,
        rate_helpers,
        ql.Actual365Fixed()
    )
    yield_curve.enableExtrapolation()

    return yield_curve

