# quantlibIBC01
My first quantlib repository
# QuantLib Risk & Pricing Demo – `quantlibIBC01`

This repository demonstrates how to use the [QuantLib](https://www.quantlib.org/) library with Python for fixed-income pricing and risk analysis. It includes:

- Yield curve construction from deposit and swap instruments
- Fixed-rate bond pricing
- Scenario analysis with shocked yield curves
- Automated testing using `pytest`
- Yield curve visualization with `matplotlib`

---

## 📦 Installation

Set up your environment:

```bash
# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
quantlibIBC01/
├── bond_pricing.py         # Bond pricing logic using QuantLib
├── yield_curve.py          # Yield curve builder with deposit + swap inputs
├── plot_yield_curve.py     # Generates and saves yield curve plots (base + shocked)
├── requirements.txt        # Python dependencies
├── README.md               # Project overview and usage instructions
└── tests/
    ├── __init__.py
    └── test_bond_pricing.py  # Unit test for bond NPV
```

---

## 🧲 Features

### ✅ Bond Pricing

`bond_pricing.py` contains logic for pricing a 10-year fixed-rate bond using a market yield curve. The bond engine uses a discounting term structure and assumes annual coupons and ISDA Actual/Actual conventions.

### ✅ Yield Curve Construction

`yield_curve.py` builds a `PiecewiseLinearZero` yield curve from two types of instruments:

- **Deposits:** Short-term cash instruments (e.g., 1W, 1M)
- **Swaps:** Longer-term instruments (e.g., 2Y, 5Y, 10Y)

The combined helpers produce a smooth curve that covers the full term needed for pricing.

### ✅ Scenario Analysis & Yield Curve Plotting

`plot_yield_curve.py`:

- Builds two yield curves:
  - A base curve from current market data
  - A shocked curve with a +50bps shift
- Extracts zero rates and converts QuantLib dates to Python dates
- Plots both curves using `matplotlib`
- Saves the output as a timestamped PNG file

### ✅ Unit Testing

Simple `pytest` test case in `test_bond_pricing.py`:

- Validates that the bond Net Present Value (NPV) falls within a rough sanity range

Run with:

```bash
PYTHONPATH=. pytest tests/
```

---

## 📊 Plotting Results

To generate and save a yield curve plot:

```bash
python plot_yield_curve.py
```

You’ll get output like:

```
Plot saved as yield_curve_comparison_20250617_150242.png
```

This image will show two yield curves over time: the current market curve and a parallel upward shift.

---

## 🛠️ Dependencies

```
QuantLib-Python
matplotlib
pytest
```

These are defined in `requirements.txt`. To add new ones:

```bash
pip install <package-name>
pip freeze > requirements.txt
```

---

## 🚀 Next Steps & Ideas

Here’s where you can take this next:

- Add support for:
  - DV01, modified duration, convexity
  - Callable or floating-rate bonds
- Export scenario results and curve points to CSV
- Integrate a CLI or web API interface
- Add multiple shock scenarios: curve steepeners, flatteners, etc.
- Introduce forward curve and implied rate modeling

---

## 📚 References

- [QuantLib Python Bindings](https://github.com/lballabio/QuantLib-SWIG)
- [QuantLib Docs & Guides](https://www.quantlib.org/documentation.shtml)
- [QuantLib GitHub](https://github.com/lballabio/QuantLib)
- [Ian Bowell on LinkedIn](https://www.linkedin.com/in/ibowell/)
---

## 👤 Author

Built by [Ian Bowell on LinkedIn](https://www.linkedin.com/in/ibowell/) 
— inspired by hands-on financial modeling, open-source quant libraries, and risk management best practices.

Feel free to fork, contribute, or reach out with suggestions!

