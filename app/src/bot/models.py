from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.utcnow)
    rating = Column(Integer, default=0)
    products = Column(JSON, default=[])  # Список товаров пользователя
    
    def __repr__(self):
        return f"<User(telegram_id={self.telegram_id}, rating={self.rating})>"

# Инициализация базы данных
engine = create_engine('sqlite:///bot.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)