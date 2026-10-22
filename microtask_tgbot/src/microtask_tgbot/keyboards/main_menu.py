from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Моя задача", callback_data="menu:task")
    builder.button(text="Статистика", callback_data="menu:statistics")
    builder.button(text="Настройки", callback_data="menu:settings")

    builder.adjust(2)

    return builder.as_markup()

def get_task_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Поставить задачу", callback_data="task:set")
    builder.button(text="Назад", callback_data="menu:main")

    builder.adjust(1)

    return builder.as_markup()

def get_settings_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Время для задачи", callback_data="menu:settings")
    builder.button(text="Назад", callback_data="menu:main")

    builder.adjust(1)

    return builder.as_markup()
