from aiogram import Bot, Dispatcher
from handlers.handlers import router as handlers_router  # Изменено для лучшей читаемости

from config import TOKEN

async def main():
    """
    Основная функция инициализации и запуска бота.
    Создает экземпляр бота, диспетчер и регистрирует обработчики.
    """
    if not TOKEN:
        raise ValueError("Токен бота не установлен. Проверьте config.py")
    
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Регистрация всех роутеров
    dp.include_router(handlers_router)

    # Запускаем бота, пропуская накопленные сообщения
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка в работе бота: {e}")
        raise