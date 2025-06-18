import QuantLib as ql
from yield_curve import build_yield_curve

def price_fixed_rate_bond():
    curve = build_yield_curve()

    face_value = 100
    issue_date = ql.Date(1, 1, 2020)
    maturity_date = ql.Date(1, 1, 2030)

    schedule = ql.Schedule(
        issue_date,
        maturity_date,
        ql.Period(ql.Annual),
        ql.TARGET(),
        ql.Unadjusted,
        ql.Unadjusted,
        ql.DateGeneration.Backward,
        False
    )

    bond = ql.FixedRateBond(
        2,  # settlement days
        face_value,
        schedule,
        [0.05],  # coupon rate
        ql.ActualActual(ql.ActualActual.ISDA)  # payment day counter
    )

    engine = ql.DiscountingBondEngine(
        ql.YieldTermStructureHandle(curve)
    )
    bond.setPricingEngine(engine)

    return bond.NPV()
