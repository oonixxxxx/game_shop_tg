from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_mainkeyboard() -> ReplyKeyboardMarkup:
    """
    Создает основную клавиатуру с кнопками Каталог и Корзина
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="Каталог")
    kb.button(text="Корзина")
    kb.adjust(2)  # Располагаем 2 кнопки в ряд
    return kb.as_markup(resize_keyboard=True)

def get_helpkeyboard() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру для меню помощи
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text='В главное меню')
    kb.button(text='Тех поддержка')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_catalog() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру для каталога товаров
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text='Посмотреть каталог товаров')
    kb.button(text='Корзина')
    kb.adjust(2)  # Добавлен adjust для правильного отображения
    return kb.as_markup(resize_keyboard=True)