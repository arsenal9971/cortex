import pytest

from rest_framework.test import APIClient


@pytest.fixture
def drf_client():
    return APIClient()


@pytest.yield_fixture
def caplog(caplog):
    import logging

    restore = []
    for logger in logging.Logger.manager.loggerDict.values():
        try:
            if not logger.propagate:
                logger.propagate = True
                restore += [logger]
        except AttributeError:
            pass
    yield caplog
    for logger in restore:
        logger.propagate = False
