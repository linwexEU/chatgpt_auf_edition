from fastapi import APIRouter, Depends
from app.styles.dao import StylesDAO
from app.styles.schemas import Style
from app.users.dependencies import get_current_user
from app.users.schemas import User


router = APIRouter(
    prefix="/style",
    tags=["Styles"]
)


@router.post("/add_style")
async def add_style(style_data: Style, current_user: User = Depends(get_current_user)): 
    await StylesDAO.add(
        name=style_data.name, 
        style=style_data.style, 
        style_user_id=current_user["Users"].user_id
    )
    return {"message": f"Your style: {style_data.name} was added!"}


@router.get("/get_styles")
async def get_styles(current_user: User = Depends(get_current_user)): 
    return [item.name for item in (await StylesDAO.get_all())]