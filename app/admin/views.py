from sqladmin import ModelView
from app.styles.models import Styles
from app.users.models import Users


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.user_id, Users.username]
    column_details_exclude_list = [Users.hashed_password]
    name = "Пользователь" 
    name_plural = "Пользователи" 
    icon = "fa-solid fa-user"


class StylesAdmin(ModelView, model=Styles):
    column_list = [Styles.style_id, Styles.name]
    name = "Стиль" 
    name_plural = "Стили" 
    icon = "fa-solid fa-border-top-left"