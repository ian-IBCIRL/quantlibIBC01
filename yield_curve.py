import QuantLib as ql

def build_yield_curve():
    today = ql.Date.todaysDate()
    ql.Settings.instance().evaluationDate = today

    calendar = ql.TARGET()
    deposit_rates = [(1, ql.Weeks, 0.0015), (1, ql.Months, 0.002)]
    deposits = [ql.DepositRateHelper(ql.QuoteHandle(ql.SimpleQuote(rate)),
                                     ql.Period(*tenor),
                                     2, calendar, ql.ModifiedFollowing,
                                     False, ql.Actual360())
                for tenor, _, rate in deposit_rates]

    yield_curve = ql.PiecewiseLinearZero(today, deposits, ql.Actual365Fixed())
    return yield_curve
