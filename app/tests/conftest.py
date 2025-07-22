import pytest
from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
import logging

@pytest.fixture(autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.DEBUG)

@pytest.fixture
def storage():
    return MemoryStorage()

@pytest.fixture
def bot():
    return Bot(token="test_token")

@pytest.fixture
def dp(storage):
    dp = Dispatcher(storage=storage)
    yield dp