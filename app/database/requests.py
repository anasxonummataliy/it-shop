from app.database.models import async_session, User, Item, Category
from sqlalchemy import update, delete, select


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_catagory():
    async with async_session() as session:
        result = await session.scalars(select(Category))
        return result.all()


async def get_items_by_category(category_id: int):
    async with async_session() as session:
        result = await session.scalars(
            select(Item).where(Item.category_id == category_id)
        )
        return result.all()


async def get_item_by_id(item_id: int):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))
