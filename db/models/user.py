from ..base_class import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship

class User(Base):
    id = Column(Integer,primary_key = True, index=True)
    user_name=Column(String,nullable= False,)
    password_hass=Column(String,nullable= False,)
    name = Column(String,nullable= False)
    surname = Column(String,nullable= False)
    
    posts=relationship("Post",back_populates="user")
    comments=relationship("Comment",back_populates="user")
    items=relationship("Item",back_populates="user")