import asyncio

# Основной запуск бота
from bot.bot import main

if __name__ == "__main__":
    print('Программа запускается...')
    
    # Запуск бота с обработкой асинхронных событий
    print('Бот запускается...')
    try:
        asyncio.run(main()) # Основная точка входа для бота
        print('Бот успешно запущен...')
    except Exception as e:
        print(f'Ошибка при запуске бота: {e}')
    finally:
        print('Программа завершена...')