import logging
import os

import structlog


def setup_logging() -> None:
    app_env = os.getenv("APP_ENV", "development").lower()
    is_development = app_env == "development"

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
    )

    renderer = (
        structlog.dev.ConsoleRenderer()
        if is_development
        else structlog.processors.JSONRenderer()
    )

    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        renderer,
    ]

    structlog.configure(
        processors=processors,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


def get_logger(name: str = __name__):
    return structlog.get_logger(name)


def bind_trace_id(trace_id: str) -> None:
    structlog.contextvars.bind_contextvars(trace_id=trace_id)


def clear_trace_id() -> None:
    structlog.contextvars.clear_contextvars()
