from aiogram import Bot, Dispatcher
from handlers.handlers import router as handlers_router
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

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

def setup_logging():
    """Настройка системы логирования"""
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=Config.LOG_LEVEL,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler(
                log_dir / 'bot.log',
                maxBytes=10**6,
                backupCount=5
            ),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

logger = setup_logging()


import asyncio
from aiogram import Bot, Dispatcher

from config import Config
from middlewares.error_middleware import register_error_middleware
from handlers import start, help, catalog

# Настройка логирования
logger = setup_logging()

async def main():
    try:
        logger.info("Starting bot...")
        
        bot = Bot(token=Config.BOT_TOKEN)
        dp = Dispatcher()

        # Регистрация middleware
        register_error_middleware(dp)

        # Регистрация роутеров
        dp.include_routers(
            start.router,
            help.router,
            catalog.router
        )

        # Запуск бота
        await bot.delete_webhook(drop_pending_updates=True)
        logger.info("Bot started successfully")
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.critical(f"Bot failed to start: {e}")
        raise
    finally:
        logger.info("Bot stopped")