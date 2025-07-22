from aiogram import Router, types
from aiogram.filters import Command
from sqlalchemy.orm import Session
from models import User

from assets.keyboard import get_mainkeyboard

router = Router(name="start-router")

@router.message(Command("start"))
async def cmd_start(message: types.Message, db: Session):
    """
    Обработчик команды /start
    """
    try:
        # Проверяем есть ли пользователь в БД
        user = db.query(User).filter(User.telegram_id == message.from_user.id).first()
        
        if not user:
            # Создаем нового пользователя
            new_user = User(telegram_id=message.from_user.id)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            welcome_text = "Добро пожаловать! Вы успешно зарегистрированы."
        else:
            welcome_text = "С возвращением!"
        
        await message.answer(
            f"{welcome_text} Это стартовое сообщение бота.",
            reply_markup=get_mainkeyboard()
        )
    except Exception as e:
        print(f"Ошибка в обработчике start: {e}")
        return 0