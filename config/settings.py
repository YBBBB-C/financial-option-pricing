"""Configuration settings for the financial modeling project.
全局配置
"""

import os
from pathlib import Path
from typing import Dict, Any

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
BLOOMBERG_DATA_DIR = DATA_DIR / "bloomberg"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
TESTS_DIR = PROJECT_ROOT / "tests"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
LOGS_DIR = PROJECT_ROOT / "logs"
BASELINE_DIR = PROJECT_ROOT / "tests" / "regression" / "baselines"

def ensure_directories() -> None:
    """Create required directories on demand.
    按需创建所需目录 - 避免在导入时创建目录
    """
    for directory in [BLOOMBERG_DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, LOGS_DIR, BASELINE_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

# ============================================================================
# GBM PARAMETERS (Geometric Brownian Motion Parameters)
# 几何布朗运动参数 - 用于资产价格路径模拟
# ============================================================================
GBM_DEFAULT_PARAMS: Dict[str, float] = {
    "mu": 0.08,          # Drift coefficient / 漂移系数 (年收益率)
    "sigma": 0.20,       # Volatility / 波动率 (年化波动率)
    "S0": 100.0,         # Initial stock price / 初始股价
    "T": 1.0,            # Time horizon / 时间范围 (years / 年)
    "dt": 0.01,          # Time step / 时间步长 (Δt in discrete simulation / 离散化模拟中的Δt)
    "n_steps": 252,      # Number of steps / 步数 (trading days per year / 每年交易日)
}

# ============================================================================
# OPTION PRICING PARAMETERS
# 期权定价参数
# ============================================================================
OPTION_PRICING: Dict[str, Any] = {
    "risk_free_rate": 0.05,    # Risk-free rate / 无风险利率
    "mc_paths": 10000,         # Monte Carlo simulations / 蒙特卡洛路径数
    "mc_steps": 252,           # Trading days per year / 每年交易日
    "call_threshold": 0.0001,  # Numerical precision / 数值精度阈值
}

# ============================================================================
# BLOOMBERG API CONFIGURATION
# Bloomberg API 配置 - 市场数据获取
# ============================================================================
BLOOMBERG: Dict[str, Any] = {
    "host": os.getenv("BLOOMBERG_HOST", "localhost"),
    "port": int(os.getenv("BLOOMBERG_PORT", "8194")),
    "timeout": 30,              # Connection timeout (seconds) / 连接超时
    "retries": 3,               # Retry attempts / 重试次数
    "cache_enabled": True,      # Enable data caching / 启用数据缓存
}

# ============================================================================
# DATA VALIDATION RULES
# 数据验证规则
# ============================================================================
DATA_VALIDATION: Dict[str, Any] = {
    "min_data_points": 252,     # Minimum historical data (1 year) / 最少历史数据点
    "nan_threshold": 0.1,       # Max allowed missing data % / 最大允许缺失数据比例
    "outlier_std_dev": 5.0,     # Outlier threshold (5 std devs) / 异常值阈值
    "price_change_limit": 0.20, # Max daily price change % / 最大单日价格变化
}

# ============================================================================
# BACKTESTING PARAMETERS
# 回测参数
# ============================================================================
BACKTEST: Dict[str, Any] = {
    "initial_capital": 100000,  # Starting capital / 初始资本
    "commission": 0.001,        # Trading commission (0.1%) / 交易佣金
    "slippage": 0.0001,         # Price slippage / 价格滑点
}

# ============================================================================
# EXPERIMENT TRACKING (Skore/MLflow)
# 实验追踪配置 - 用于模型对比和参数管理
# ============================================================================
EXPERIMENT: Dict[str, Any] = {
    "project_name": "option-pricing-experiments",
    "tracking_uri": os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000"),
    "auto_log": True,           # Automatic parameter logging / 自动参数记录
}

# Debug mode
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
