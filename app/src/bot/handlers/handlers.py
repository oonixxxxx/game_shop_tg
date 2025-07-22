from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from assets.keyboard import get_mainkeyboard, get_helpkeyboard, get_catalog

router = Router()

@router.message(Command("start"))
async def cmd_start(msg: Message):
    """
    Обработчик команды /start
    Приветствует пользователя и показывает основное меню
    """
    await msg.answer(
        "Добро пожаловать! Это стартовое сообщение бота.",
        reply_markup=get_mainkeyboard()
    )

@router.message(Command('help'))
async def cmd_help(msg: Message):
    """
    Обработчик команды /help
    Показывает справку и меню помощи
    """
    await msg.answer(
        'Здесь вы можете получить помощь. Выберите опцию:',
        reply_markup=get_helpkeyboard()
    )

@router.message(Command('catalog'))
async def cmd_catalog(msg: Message):
    """
    Обработчик команды /catalog
    Показывает каталог товаров
    """
    await msg.answer(
        'Наш каталог товаров:',
        reply_markup=get_catalog()
    )