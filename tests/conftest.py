import pytest
from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage

@pytest.fixture
def storage():
    return MemoryStorage()

@pytest.fixture
def bot():
    return Bot(token="test_token")

@pytest.fixture
def dp(storage):
    return Dispatcher(storage=storage)