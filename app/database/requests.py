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
        return await session.scalars(select(Category))


async def get_items_by_category(category_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.category == category_id))


async def get_items(item_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.id == item_id))
