from aiogram import Router, types
from aiogram.filters import Command

from assets.keyboard import get_catalog

router = Router(name="catalog-router")

@router.message(Command('catalog'))
async def cmd_catalog(message: types.Message):
    """
    Обработчик команды /catalog
    """
    try:
        await message.answer(
            'Наш каталог товаров:',
            reply_markup=get_catalog()
        )
    except Exception as e:
        logger.error(f"Ошибка в обработчике catalog: {e}")
        raise