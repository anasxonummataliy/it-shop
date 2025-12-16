from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Assalomu alaykum, bizning botimizga xush kelibsiz,")