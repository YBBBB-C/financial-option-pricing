"""Data validation and preprocessing utilities.
数据验证和预处理工具
"""

import numpy as np
import pandas as pd
from typing import Tuple, Dict, Any
from config.settings import DATA_VALIDATION
from utils.logger import setup_logger

logger = setup_logger(__name__)

def validate_price_series(prices: pd.Series) -> Tuple[bool, str]:
    """Validate price time series for data quality.
    验证价格时间序列的数据质量
    
    Args:
        prices: Price series / 价格序列
    
    Returns:
        Tuple of (is_valid, message) / 验证结果和信息
    """
    # Check minimum data points
    if len(prices) < DATA_VALIDATION["min_data_points"]:
        return False, f"Insufficient data: {len(prices)} < {DATA_VALIDATION['min_data_points']}"
    
    # Check for NaN values
    nan_ratio = prices.isna().sum() / len(prices)
    if nan_ratio > DATA_VALIDATION["nan_threshold"]:
        return False, f"Too many NaN values: {nan_ratio:.2%}"
    
    # Fill forward missing values
    prices = prices.fillna(method='ffill').fillna(method='bfill')
    
    # Check for outliers
    returns = prices.pct_change().dropna()
    std = returns.std()
    outliers = np.abs(returns) > DATA_VALIDATION["outlier_std_dev"] * std
    if outliers.sum() > 0:
        logger.warning(f"Found {outliers.sum()} outliers in returns")
    
    return True, "Data validation passed"

def calculate_log_returns(prices: pd.Series) -> pd.Series:
    """Calculate log returns from price series.
    从价格序列计算对数收益率
    
    Args:
        prices: Price series / 价格序列
    
    Returns:
        Log returns / 对数收益率
    """
    return np.log(prices / prices.shift(1)).dropna()

def calculate_realized_volatility(returns: pd.Series, window: int = 20) -> pd.Series:
    """Calculate rolling realized volatility.
    计算滚动已实现波动率
    
    Args:
        returns: Return series / 收益率序列
        window: Rolling window size / 滚动窗口大小
    
    Returns:
        Rolling volatility / 滚动波动率
    """
    return returns.rolling(window).std() * np.sqrt(252)  # Annualized

def detect_volatility_regime(volatility: pd.Series, threshold: float = None) -> str:
    """Detect current volatility regime.
    检测当前波动率制度
    
    Args:
        volatility: Volatility series / 波动率序列
        threshold: Regime threshold / 制度阈值
    
    Returns:
        Regime label ('low', 'medium', 'high') / 制度标签
    """
    from config.constants import VOLATILITY_REGIME_THRESHOLD
    if threshold is None:
        threshold = VOLATILITY_REGIME_THRESHOLD
    
    current_vol = volatility.iloc[-1]
    if current_vol < threshold * 0.8:
        return "low"
    elif current_vol > threshold * 1.2:
        return "high"
    else:
        return "medium"
