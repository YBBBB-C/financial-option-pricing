"""Structured logging configuration.
日志配置 - 用于调试和生产环境
"""

import logging
from pathlib import Path
from config.settings import LOGS_DIR, DEBUG

# Ensure logs directory exists
LOGS_DIR.mkdir(parents=True, exist_ok=True)

def setup_logger(name: str, level: int = None) -> logging.Logger:
    """Setup logger with console and file handlers.
    配置具有控制台和文件处理的日志记录器
    
    Args:
        name: Logger name / 日志记录器名称
        level: Logging level / 日志级别
    
    Returns:
        Configured logger / 配置完成的日志记录器
    """
    if level is None:
        level = logging.DEBUG if DEBUG else logging.INFO
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid duplicate handlers
    if logger.hasHandlers():
        return logger
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # File handler
    log_file = LOGS_DIR / f"{name}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Default logger
logger = setup_logger(__name__)
