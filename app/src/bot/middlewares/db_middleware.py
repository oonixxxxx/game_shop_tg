from sqlalchemy.orm import Session
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Any
from aiogram.types import Message

from models import Session as DBSession

class DBMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any]
    ) -> Any:
        async with DBSession() as session:
            data["db"] = session
            return await handler(event, data)