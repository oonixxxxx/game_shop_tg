from aiogram import Bot, Dispatcher
from config import Config
from middlewares.error_middleware import register_error_middleware
from middlewares.db_middleware import DBMiddleware
from handlers import start, help, catalog
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

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

async def main():
    try:
        logger.info("Starting bot...")
        
        bot = Bot(token=Config.BOT_TOKEN)
        dp = Dispatcher()

        # Регистрация middleware
        dp.update.middleware(DBMiddleware())
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