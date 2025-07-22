import pytest
from aiogram import types
from handlers.start import cmd_start

@pytest.mark.asyncio
async def test_start_handler():
    message = types.Message(
        message_id=1,
        date=None,
        chat=types.Chat(id=1, type='private'),
        text='/start'
    )
    await cmd_start(message)
    # Проверки можно добавить с помощью моков