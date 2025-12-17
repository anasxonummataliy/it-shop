from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_catagory, get_items_by_category

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Katolog", callback_data="catalog")],
        [InlineKeyboardButton(text="Kontakt", callback_data="contact")],
    ]
)


async def categories():
    all_categories = await get_catagory()
    ikb = InlineKeyboardBuilder()
    for category in all_categories:
        ikb.row(
            InlineKeyboardButton(
                text=category.name, callback_data=f"category_{category.id}"
            )
        )
    ikb.row(InlineKeyboardButton(text="Back", callback_data="start"))
    return ikb.as_markup()


async def items_keyboard(category_id: int):
    all_items = await get_items_by_category(category_id)
    ikb = InlineKeyboardBuilder()
    for items in all_items:
        ikb.row(InlineKeyboardButton(text=items.name, callback_data=f"item_{items.id}"))
    ikb.row(InlineKeyboardButton(text="Back", callback_data="catalog"))
    return ikb.as_markup()


async def back_to_category(category_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Back", callback_data=f"category_{category_id}")]
        ]
    )
