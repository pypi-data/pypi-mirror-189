import logging
from typing import Iterable, Optional, Union

from dcclog.cipher import Cipher
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
    color: bool = True,
    cipher: Optional[Cipher] = None,
) -> None:
    root = getLogger(level=level)
    if not root.handlers:
        handlers: list[logging.Handler] = []
        console_hdlr = logging.StreamHandler()
        console_hdlr.setFormatter(Formatter(color=color))
        handlers.append(console_hdlr)
        if filename:
            file_hdlr = logging.FileHandler(filename)
            file_hdlr.setFormatter(Formatter(cipher=cipher))
            handlers.append(file_hdlr)

        for h in handlers:
            root.addHandler(h)
