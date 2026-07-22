# Financial Option Pricing & GBM Simulator

A comprehensive financial modeling framework for simulating asset prices using Geometric Brownian Motion (GBM), pricing European options via Monte Carlo and Black-Scholes, and validating model assumptions against real Bloomberg market data.

## 📊 Project Structure

```
financial-option-pricing/
├── data/                    # Market data storage
│   ├── bloomberg/          # Bloomberg data ingestion
│   ├── raw/                # Raw market data
│   └── processed/          # Cleaned & validated data
├── models/
│   ├── gbm/                # GBM simulation engine
│   ├── pricing/            # Option pricing engines (BS, MC)
│   └── assumptions/        # Assumption validation & diagnostics
├── dashboard/              # Streamlit visualization
├── evaluation/             # Skore experiment tracking
├── tests/
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   └── regression/        # Regression tests with baselines
├── config/                # Configuration & constants
├── utils/                 # Utilities (logging, validation)
├── notebooks/             # Jupyter notebooks for exploration
├── docs/                  # Documentation
└── requirements.txt       # Python dependencies
```

## 🚀 Quick Start

```bash
git clone https://github.com/YBBBB-C/financial-option-pricing.git
cd financial-option-pricing
pip install -r requirements.txt
python -c "from config.settings import ensure_directories; ensure_directories()"
streamlit run dashboard/app.py
```

## ✨ Features

- **GBM Simulator**: Price paths with calibrated parameters
- **Option Pricing**: Black-Scholes & Monte Carlo methods
- **Model Validation**: Assumption testing against market data
- **Dashboard**: Real-time metrics & visualizations
- **Experiment Tracking**: Skore-powered model comparison
- **Regression Testing**: Baseline comparison for model stability

## 📈 Development Status

- [✅] Project Structure & Setup
- [🔄] Bloomberg Data Connector
- [🔄] GBM Simulator
- [🔄] Pricing Engines (BS + MC)
- [🔄] Skore Integration & Evaluation
- [🔄] Streamlit Dashboard
- [🔄] Comprehensive Test Suite
- [🔄] Backtesting Framework

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v --cov=.

# Run only unit tests
pytest tests/unit -v

# Run regression tests
pytest tests/regression -v

# Run with coverage report
pytest tests/ --cov=. --cov-report=html
```

## 🔧 Configuration

Edit `config/settings.py` to customize:
- GBM parameters
- Option pricing parameters
- Bloomberg API settings
- Data validation rules

## 📚 Documentation

See `docs/` for detailed guides on:
- Model architecture & theory
- Bloomberg API setup
- Backtesting methodology
- Dashboard metrics & KPIs
