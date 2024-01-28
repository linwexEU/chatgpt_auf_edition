from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base 


class Users(Base): 
    __tablename__ = "users" 

    user_id: Mapped[int] = mapped_column(primary_key=True, nullable=False) 
    username: Mapped[str] = mapped_column(nullable=False) 
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    last_query: Mapped[str] = mapped_column(nullable=False) 
    last_answer: Mapped[str] = mapped_column(nullable=False)

    style_creator = relationship("Styles", back_populates="name_creator")

    def __str__(self): 
        return self.username


