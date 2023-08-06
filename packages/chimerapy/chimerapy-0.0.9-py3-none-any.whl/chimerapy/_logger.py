# Setup the logging for the library
# References:
# https://docs.python-guide.org/writing/logging/
# https://stackoverflow.com/questions/13649664/how-to-use-logging-with-pythons-fileconfig-and-configure-the-logfile-filename
import logging.config
import os

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        }
    },
    "loggers": {
        "chimerapy": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "chimerapy-worker": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "chimerapy-networking": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "chimerapy-subprocess": {
            "handlers": [],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# Setup the logging configuration
def setup():

    # Setting up the configureation
    logging.config.dictConfig(LOGGING_CONFIG)


def getLogger(name: str):

    # Get the logging
    logger = logging.getLogger(name)

    # Ensure that the configuration is set
    debug_loggers = os.environ.get("CHIMERAPY_DEBUG_LOGGERS", "").split(os.pathsep)
    if name in debug_loggers:
        logger.setLevel(logging.DEBUG)

    return logger
