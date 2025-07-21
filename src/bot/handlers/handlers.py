from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from assets.keyboard import get_mainkeyboard, get_helpkeyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(msg: Message):
    await msg.answer(
        "start text",
        reply_markup=get_mainkeyboard()
    )

@router.message(Command('help'))
async def cmd_help(msg: Message):
    await msg.answer(
        'help text',
        reply_markup=get_helpkeyboard()
    )

@router.message(Command('catalog'))
async def cmd_catalog(msg: Message):
    await msg.answer(
        'catalog text',
        reply_markup=get_catalog()
    )