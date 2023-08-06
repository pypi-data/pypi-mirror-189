import logging
from typing import Iterable, Optional, Union

from dcclog.formatters import Formatter


def getLogger(
    name: Optional[str] = None,
    *,
    level: Union[str, int, None] = None,
    handlers: Union[Iterable[logging.Handler], logging.Handler, None] = None,
) -> logging.Logger:
    logger = logging.getLogger(name)
    if level is not None:
        logger.setLevel(level)
    if isinstance(handlers, logging.Handler):
        logger.addHandler(handlers)
    elif isinstance(handlers, Iterable):
        for hdlr in handlers:
            logger.addHandler(hdlr)
    return logger


def default_config(
    level: int = logging.WARNING,
    filename: Optional[str] = None,
    color: Optional[bool] = None,
) -> None:
    root = getLogger(level=level)
    if not root.handlers:
        if filename:
            fmt = Formatter(color=False if color is None else color)
            handler: logging.Handler = logging.FileHandler(filename)
        else:
            fmt = Formatter(color=True if color is None else color)
            handler = logging.StreamHandler()
        handler.setFormatter(fmt)
        root.addHandler(handler)
