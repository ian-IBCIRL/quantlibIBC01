import QuantLib as ql
import matplotlib.pyplot as plt
from datetime import datetime

def build_yield_curve(shock=0.0):
    today = ql.Date.todaysDate()
    ql.Settings.instance().evaluationDate = today
    calendar = ql.TARGET()

    deposit_rates = [(1, ql.Weeks, 0.0015 + shock), (1, ql.Months, 0.002 + shock)]
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

    swap_rates = [(2, ql.Years, 0.005 + shock), (5, ql.Years, 0.01 + shock), (10, ql.Years, 0.015 + shock)]
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

    rate_helpers = deposit_helpers + swap_helpers
    curve = ql.PiecewiseLinearZero(today, rate_helpers, ql.Actual365Fixed())
    curve.enableExtrapolation()
    return curve

def get_curve_data(curve):
    dates = curve.dates()
    rates = [curve.zeroRate(d, ql.Actual365Fixed(), ql.Continuous).rate() for d in dates]
    py_dates = [ql.Date.to_date(d) for d in dates]
    return py_dates, rates

def plot_yield_curve():
    base_curve = build_yield_curve()
    shocked_curve = build_yield_curve(shock=0.005)

    dates1, rates1 = get_curve_data(base_curve)
    dates2, rates2 = get_curve_data(shocked_curve)

    plt.figure(figsize=(10, 5))
    plt.plot(dates1, rates1, label="Base Curve")
    plt.plot(dates2, rates2, label="+50bps Shock", linestyle='--')
    plt.title("Zero Yield Curve Comparison")
    plt.xlabel("Date")
    plt.ylabel("Zero Rate")
    plt.grid(True)
    plt.legend()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"yield_curve_comparison_{timestamp}.png"
    plt.savefig(filename)
    print(f"Plot saved as {filename}")

if __name__ == "__main__":
    plot_yield_curve()
