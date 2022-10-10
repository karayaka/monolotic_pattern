from ..base_class import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship


class Item(Base):
    id = Column(Integer,primary_key = True, index=True)
    name=Column(String,nullable= False,)
    desc=Column(String,nullable= False,)

    user_id=Column(Integer,ForeignKey("User.id"))
    user=relationship("User",back_populates="items")