import os
from dotenv import load_dotenv
import logging

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot.db')

    @classmethod
    def validate(cls):
        if not cls.BOT_TOKEN:
            raise ValueError('BOT_TOKEN не установлен в .env файле')

Config.validate()