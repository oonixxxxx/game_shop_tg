import os
from dotenv import load_dotenv
import logging

# Загрузка переменных окружения
load_dotenv()

class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    @classmethod
    def validate(cls):
        if not cls.BOT_TOKEN:
            raise ValueError('BOT_TOKEN не установлен в .env файле')

# Валидация конфигурации при импорте
Config.validate()