import pytest
from aiogram import types
from src.bot.handlers.handlers import cmd_start, cmd_help, cmd_catalog

@pytest.mark.asyncio
async def test_start_handler():
    message = types.Message(
        message_id=1, 
        date=None, 
        chat=types.Chat(id=1, type='private'),
        text='/start'
    )
    result = await cmd_start(message)
    assert result is None  # Проверяем, что функция выполняется без ошибок

@pytest.mark.asyncio
async def test_help_handler():
    message = types.Message(
        message_id=1, 
        date=None, 
        chat=types.Chat(id=1, type='private'),
        text='/help'
    )
    result = await cmd_help(message)
    assert result is None

@pytest.mark.asyncio
async def test_catalog_handler():
    message = types.Message(
        message_id=1, 
        date=None, 
        chat=types.Chat(id=1, type='private'),
        text='/catalog'
    )
    result = await cmd_catalog(message)
    assert result is None