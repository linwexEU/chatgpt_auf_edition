from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from database import Base 


class Styles(Base): 
    __tablename__ = "styles" 

    style_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    style: Mapped[str] = mapped_column(nullable=False)
    style_user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    
    name_creator = relationship("Users", back_populates="style_creator")

    def __str__(self): 
        return self.name





