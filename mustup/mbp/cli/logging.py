import logging
import sys

logger = logging.getLogger(
    __name__,
)


def set_up(
            level,
        ):
    top_logger = logging.getLogger(
        name=None,
    )

    handler = logging.StreamHandler(
        stream=sys.stderr,
    )

    formatter = logging.Formatter(
        datefmt=None,
        fmt='%(name)s: %(levelname)s: %(message)s',
        style='%',
    )

    handler.setFormatter(
        formatter,
    )

    top_logger.addHandler(
        handler,
    )

    top_logger.setLevel(
        level,
    )
