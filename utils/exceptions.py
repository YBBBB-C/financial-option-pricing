""" Error handling and custom exceptions.
错误处理和自定义异常
"""

class FinancialModelError(Exception):
    """ Base exception for financial modeling errors.
    财务建模错误的基类异常
    """
    pass

class DataValidationError(FinancialModelError):
    """ Raised when data validation fails.
    数据验证失败时抛出
    """
    pass

class ModelCalibrationError(FinancialModelError):
    """ Raised when model calibration fails.
    模型校准失败时抛出
    """
    pass

class PricingError(FinancialModelError):
    """ Raised when option pricing fails.
    期权定价失败时抛出
    """
    pass

class BloombergConnectionError(FinancialModelError):
    """ Raised when Bloomberg connection fails.
    Bloomberg连接失败时抛出
    """
    pass
