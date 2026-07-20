"""Mathematical and financial constants.
数学和财务常数 - 全局常数定义
"""

import math

# ============================================================================
# MATHEMATICAL CONSTANTS
# 数学常数
# ============================================================================
PI = math.pi
E = math.e
SQRT_2PI = math.sqrt(2 * PI)  # √(2π) used in normal distribution / 用于正态分布
SQRT_2 = math.sqrt(2)

# ============================================================================
# FINANCIAL CALENDAR CONSTANTS
# 财务日历常数
# ============================================================================
TRADING_DAYS_PER_YEAR = 252    # Standard trading days / 标准交易日
TRADING_HOURS_PER_DAY = 6.5    # NYSE hours: 9:30 AM - 4:00 PM / NYSE交易时间
TRADING_MINUTES_PER_DAY = TRADING_HOURS_PER_DAY * 60

# ============================================================================
# OPTION TYPES AND STYLES
# 期权类型
# ============================================================================
OPTION_TYPE_CALL = "call"      # Call option / 看涨期权
OPTION_TYPE_PUT = "put"        # Put option / 看跌期权
OPTION_STYLE_EUROPEAN = "european"  # European option / 欧式期权
OPTION_STYLE_AMERICAN = "american"  # American option / 美式期权

# ============================================================================
# BLOOMBERG DATA FIELDS
# Bloomberg 市场数据字段
# ============================================================================
BBG_FIELDS = {
    "PX_LAST": "Last Price",           # 最后价格
    "PX_OPEN": "Open Price",           # 开盘价
    "PX_HIGH": "High Price",           # 最高价
    "PX_LOW": "Low Price",             # 最低价
    "PX_VOLUME": "Volume",             # 成交量
    "VOLATILITY": "Implied Volatility", # 隐含波动率
    "PX_BID": "Bid Price",             # 买价
    "PX_ASK": "Ask Price",             # 卖价
}

# ============================================================================
# STATISTICAL TEST THRESHOLDS
# 统计测试阈值
# ============================================================================
NORMALITY_ALPHA = 0.05                 # Significance level (Shapiro-Wilk) / 显著性水平
VOLATILITY_REGIME_THRESHOLD = 0.25     # High volatility threshold / 高波动率阈值
RESIDUAL_AUTOCORR_LAG = 20             # Autocorrelation lags to test / 自相关检验滞后期数
ADF_P_VALUE_THRESHOLD = 0.05           # ADF test p-value threshold / ADF检验p值阈值

# ============================================================================
# NUMERICAL PRECISION CONSTANTS
# 数值精度常数
# ============================================================================
MIN_PRICE = 1e-6                       # Minimum price for numerical stability / 最小价格
MAX_ITERATIONS = 1000                 # Maximum iterations for numerical methods / 最大迭代次数
CONVERGENCE_TOLERANCE = 1e-8            # Convergence tolerance / 收敛容差
