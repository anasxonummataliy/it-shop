from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb
from app.database.requests import set_user, get_items


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await set_user(message.from_user.id)
    await message.answer(
        "Assalomu alaykum, bizning botimizga xush kelibsiz,", reply_markup=kb.menu
    )


@router.callback_query(F.data == "start")
async def callback_start(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('It shop', reply_markup=kb.menu)


@router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text(
        text="Tovarlar toifalarini tanlang", reply_markup=await kb.categories()
    )


@router.callback_query(F.startswith("category_"))
async def category(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text(
        "kategoriya bo'yicha mahsulotni tanlang",
        reply_markup=await kb.get_items(callback.data.split("_")[1]),
    )


@router.callback_query(F.startswith("item_"))
async def item_handler(callback: CallbackQuery):
    item = await get_items(callback.data.split("_")[1])
    await callback.answer("")
    await callback.message.answer(
        f"{item.name}\n\n {item.description} \n\n Narx: {item.price}",
        reply_markup=await kb.back_to_category(item.category),
    )
