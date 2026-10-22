from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from microtask_tgbot.keyboards.main_menu import get_main_menu, get_task_menu, get_settings_menu
from microtask_tgbot.states.user_states import MenuStates
from datetime import date
from sqlalchemy import select, func
from microtask_tgbot.database import session_maker, Task

router = Router(name="menu")

@router.callback_query(F.data == "menu:main")
async def show_main_menu(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MenuStates.main_menu)
    await callback.message.edit_text(
        "Главное меню\nВыберите действие:",
        reply_markup=get_main_menu()
    )
    await callback.answer()

@router.callback_query(F.data == "menu:task")
async def show_task_menu(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MenuStates.task_menu)
    await callback.message.edit_text(
        "Меню задач",
        reply_markup=get_task_menu()
    )
    await callback.answer()

@router.callback_query(F.data == "menu:settings")
async def show_settings_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        "Настройки",
        reply_markup=get_settings_menu()
    )
    await callback.answer()

@router.callback_query(F.data == "menu:statistics")
async def show_statistics(callback: CallbackQuery):
    user_id = callback.from_user.id
    today = date.today()

    async with session_maker() as session:
        completed = await session.scalar(
            select(func.count()).where(
                Task.user_id == user_id,
                Task.task_date == today,
                Task.is_completed == True
            )
        ) or 0

        not_completed = await session.scalar(
            select(func.count()).where(
                Task.user_id == user_id,
                Task.task_date == today,
                Task.is_completed == False
            )
        ) or 0

        total = completed + not_completed

        if total == 0:
            text = "Статистика задач\n\nПока нет задач."
        else:
            percent = round(completed / total * 100)
            text = (
                f"Статистика\n\n"
                f"Выполнено: <b>{completed}</b>\n"
                f"Не выполнено: <b>{not_completed}</b>\n"
                f"Процент выполнения: <b>{percent}%</b>"
            )

        await callback.message.edit_text(
            text,
            reply_markup=get_main_menu()
        )
        await callback.answer()
