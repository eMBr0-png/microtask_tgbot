from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from src.microtask_tgbot.config import settings
from src.microtask_tgbot.handlers import start
import socket
from aiohttp import TCPConnector
from aiogram.client.session.aiohttp import AiohttpSession

async def main():
    session = AiohttpSession()
    session._connector_init["family"] = socket.AF_INET6

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        session=session
    )
    dp = Dispatcher()

    dp.include_router(start.router)

    await dp.start_polling(bot)
