from bond_pricing import price_fixed_rate_bond

def test_bond_npv():
    npv = price_fixed_rate_bond()
    assert npv > 90 and npv < 110  # Rough sanity check
