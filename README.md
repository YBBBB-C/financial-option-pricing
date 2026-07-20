
# Financial Option Pricing & GBM Simulator

A comprehensive financial modeling framework for simulating asset prices using Geometric Brownian Motion (GBM), pricing European options via Monte Carlo and Black-Scholes, and validating model assumptions against real Bloomberg market data.

## 📊 Project Structure
financial-option-pricing/ ├── data/ # Market data storage │ ├── bloomberg/ # Bloomberg data ingestion │ ├── raw/ # Raw market data │ └── processed/ # Cleaned & validated data ├── models/ │ ├── gbm/ # GBM simulation engine │ ├── pricing/ # Option pricing engines (BS, MC) │ └── assumptions/ # Assumption validation & diagnostics ├── dashboard/ # Streamlit visualization ├── evaluation/ # Skore experiment tracking ├── tests/ │ ├── unit/ # Unit tests │ ├── integration/ # Integration tests │ └── regression/ # Regression tests with baselines ├── config/ # Configuration & constants ├── utils/ # Utilities (logging, validation) ├── notebooks/ # Jupyter notebooks for exploration ├── docs/ # Documentation └── requirements.txt # Python dependencies

## 🚀 Quick Start

```bash
git clone https://github.com/YBBBB-C/financial-option-pricing.git
cd financial-option-pricing
pip install -r requirements.txt
config/settings.py ensure_directories()  # Create directories
streamlit run dashboard/app.py

