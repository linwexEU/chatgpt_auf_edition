from app.dao.base import BaseDAO
from sqlalchemy import select 
from database import async_session_maker 
from app.styles.models import Styles 
from sqlalchemy.orm import selectinload


class StylesDAO(BaseDAO): 
    model = Styles

    @classmethod 
    async def get_style(cls, name): 
        async with async_session_maker() as session: 
            query = select(cls.model.style).select_from(cls.model).where(cls.model.name == name)
            result = await session.execute(query) 
            return result.scalars().one_or_none()
        
    @classmethod 
    async def get_style_with_their_creator(cls): 
        async with async_session_maker() as session: 
            query = (
                select(cls.model)
                .options(selectinload(cls.model.name_creator))
            )
            result = await session.execute(query) 
            return result.mappings().all() 


    