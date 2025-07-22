from aiogram import Dispatcher
from aiogram.types import ErrorEvent
from typing import Callable, Awaitable, Any

import logging

logger = logging.getLogger(__name__)

async def error_handler(event: ErrorEvent, dp: Dispatcher):
    """
    Middleware для обработки ошибок
    """
    logger.error(
        "Ошибка при обработке обновления %s: %s",
        event.update.dict() if event.update else None,
        event.exception,
        exc_info=True
    )
    
    # Можно отправить сообщение пользователю
    if event.update.message:
        await event.update.message.answer(
            "Произошла ошибка. Пожалуйста, попробуйте позже."
        )

def register_error_middleware(dp: Dispatcher):
    dp.errors.register(error_handler)