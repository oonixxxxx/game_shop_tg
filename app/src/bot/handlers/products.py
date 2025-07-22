from aiogram import Router, types
from aiogram.filters import Command, Text
from sqlalchemy.orm import Session
from models import User
from datetime import datetime

router = Router(name="products-router")

@router.message(Text("Мои товары"))
async def show_products(message: types.Message, db: Session):
    user = db.query(User).filter(User.telegram_id == message.from_user.id).first()
    if user:
        products = user.products or []
        if products:
            await message.answer(f"Ваши товары:\n{'\n'.join(products)}")
        else:
            await message.answer("У вас пока нет товаров.")
    else:
        await message.answer("Сначала зарегистрируйтесь с помощью /start")

@router.message(Command("add_product"))
async def add_product(message: types.Message, db: Session):
    user = db.query(User).filter(User.telegram_id == message.from_user.id).first()
    if user:
        product_name = message.text.replace('/add_product', '').strip()
        if product_name:
            products = user.products or []
            products.append(product_name)
            user.products = products
            db.commit()
            await message.answer(f"Товар '{product_name}' добавлен!")
        else:
            await message.answer("Укажите название товара после команды /add_product")
    else:
        await message.answer("Сначала зарегистрируйтесь с помощью /start")