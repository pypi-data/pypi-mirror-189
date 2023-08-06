from typing import Any
from loguru import logger




def log(__level: int or str, __message: str, *args: Any, **kwargs: Any):
    logger.log(__level, __message, *args, **kwargs)

def warning(__message: str, *args: Any, **kwargs: Any):
    logger.log("WARNING",__message, *args, **kwargs)


def info(__message: str, *args: Any, **kwargs: Any):
    logger.log("INFO",__message, *args, **kwargs)


def error(__message: str, *args: Any, **kwargs: Any):
    logger.log("ERROR",__message *args, **kwargs)

