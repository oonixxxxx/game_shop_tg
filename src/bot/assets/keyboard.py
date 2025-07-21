from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_mainkeyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Каталог")
    kb.button(text="Корзина")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_helpkeyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='В главное меню')
    kb.button(text='Тех поддержка')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_catalog() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Посмотерть каталог товаров')
    kb.button(text='Корзина')