import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bond_pricing import price_fixed_rate_bond

def test_bond_npv():
    npv = price_fixed_rate_bond()
    assert npv > 40 and npv < 150  # Rough sanity check
