from aiogram import Router, types
from aiogram.filters import Command

from assets.keyboard import get_mainkeyboard

router = Router(name="start-router")

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start
    """
    try:
        await message.answer(
            "Добро пожаловать! Это стартовое сообщение бота.",
            reply_markup=get_mainkeyboard()
        )
    except Exception as e:
        logger.error(f"Ошибка в обработчике start: {e}")
        raise