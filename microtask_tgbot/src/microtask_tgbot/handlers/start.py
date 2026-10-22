from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from microtask_tgbot.keyboards.main_menu import get_main_menu
from microtask_tgbot.states.user_states import MenuStates
from microtask_tgbot.database import session_maker, Task, init_db

router = Router(name="start")

@router.message(CommandStart())
async def cmd_start(message: Message):
    await init_db()
    await message.answer(
        "Привет!\nЯ бот, который каждый день в заданное вами время будет спрашивать, какую микроцель вы сегодня себе поставите. \nА потом вечером того же дня будете отвечать выполнили ли вы свою задачу.\nБот будет собирать статистику, которую вы сможете просматривать.\nВыбери действие в меню:",
        reply_markup=get_main_menu()
    )
