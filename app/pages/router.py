from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from app.api.router import get_answer_from_gpt
from app.api.schemas import AufData
from app.styles.dao import StylesDAO
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.schemas import User


router = APIRouter(
    prefix="/page",
    tags=["Pages"]
)
templates = Jinja2Templates(directory="app/templates")


@router.get("/login_page") 
async def login_page(request: Request): 
    return templates.TemplateResponse(
        name="login/index.html", 
        context={"request": request}
    )

@router.get("/register_page") 
async def login_page(request: Request): 
    return templates.TemplateResponse(
        name="register/index.html", 
        context={"request": request}
    )

@router.get("/main_page") 
async def login_page(request: Request, current_user: User = Depends(get_current_user)):
    styles = [f"{item['Styles'].name} - {item['Styles'].name_creator.username }" for item in (await StylesDAO.get_style_with_their_creator())]
    return templates.TemplateResponse(
        name="main/index.html", 
        context={"request": request, "items": styles, "username": current_user["Users"].username}
    )

@router.get("/add_style_page") 
async def login_page(request: Request, current_user: User = Depends(get_current_user)):
    return templates.TemplateResponse(
        name="add_style/index.html", 
        context={"request": request, "username": current_user["Users"].username}
    )

@router.get("/answer_page")
async def check_answer(request: Request, current_user: User = Depends(get_current_user)): 
    answer = await UsersDAO.get_user(current_user["Users"].user_id)
    return templates.TemplateResponse(
        name="answer/index.html", 
        context={"request": request, "username": current_user["Users"].username, "text": answer[0].last_answer}
    )