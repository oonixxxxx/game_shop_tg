from aiogram import Bot, Dispatcher
from handlers.handlers import cmd_start, cmd_help

from config import TOKEN


# Запуск бота
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        cmd_help.router,
        cmd_start.router
    )

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)