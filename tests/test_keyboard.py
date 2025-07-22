from src.bot.assets.keyboard import get_mainkeyboard, get_helpkeyboard, get_catalog
from aiogram.types import ReplyKeyboardMarkup

def test_keyboard_creation():
    # Проверка создания клавиатур
    assert isinstance(get_mainkeyboard(), ReplyKeyboardMarkup)
    assert isinstance(get_helpkeyboard(), ReplyKeyboardMarkup)
    assert isinstance(get_catalog(), ReplyKeyboardMarkup)
    
    # Проверка количества кнопок
    assert len(get_mainkeyboard().keyboard[0]) == 2
    assert len(get_helpkeyboard().keyboard[0]) == 2
    assert len(get_catalog().keyboard[0]) == 2