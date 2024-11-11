import pytest


def for_logging():
    import json

    import logging.config
    from logging import getLogger

    with open("logging.conf") as file:
        config = json.load(file)

    logging.config.dictConfig(config)
    logger = getLogger()
    logging.info("logging is working!")

def for_logging_2():
    import json

    import logging.config
    from logging import getLogger

    with open("logging_2.conf") as file:
        config = json.load(file)

    logging.config.dictConfig(config)
    logger = getLogger()
    logging.info("logging is working!")