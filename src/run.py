import asyncio

#Запуск бота
from bot.bot import main

if __name__ == "__main__":
    print('Программа запускается...')
    
    #Запуск бота
    print('Бот запускается...')
    print('Бот запущен...')
    asyncio.run(main()) #Функция вызова бота
    print('Программа закончилась...')