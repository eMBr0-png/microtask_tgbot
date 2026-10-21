from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from src.microtask_tgbot.keyboards.main_manu import get_main_menu, get_task_menu, get_settings_menu
from src.microtask_tgbot.states.user_states import MenuStates

router = Router(name="menu")

@router.callbackquery(F.data == "menu:main")
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
