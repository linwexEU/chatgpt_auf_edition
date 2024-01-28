from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from app.admin.views import StylesAdmin, UsersAdmin
from app.api.router import router as router_gpt
from app.users.router import router as router_auth 
from app.styles.router import router as router_style 
from app.pages.router import router as router_pages
from sqladmin import Admin
from app.admin.auth import authentication_backend
from database import engine

app = FastAPI() 
app.mount("/static", StaticFiles(directory="app/templates/login/static"), name="static")

app.include_router(router_auth)
app.include_router(router_gpt)
app.include_router(router_style)
app.include_router(router_pages)


admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UsersAdmin)
admin.add_view(StylesAdmin)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)








