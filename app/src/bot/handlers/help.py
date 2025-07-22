from aiogram import Router, types
from aiogram.filters import Command

from assets.keyboard import get_helpkeyboard

router = Router(name="help-router")

@router.message(Command('help'))
async def cmd_help(message: types.Message):
    """
    Обработчик команды /help
    """
    try:
        await message.answer(
            'Здесь вы можете получить помощь. Выберите опцию:',
            reply_markup=get_helpkeyboard()
        )
    except Exception as e:
        logger.error(f"Ошибка в обработчике help: {e}")
        raise