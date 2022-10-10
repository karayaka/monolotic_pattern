from ..base_class import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    id = Column(Integer,primary_key = True, index=True)
    title=Column(String,nullable= False,)
    content=Column(String,nullable= False,)
    user_id=Column(Integer,ForeignKey("User.id"))
    user=relationship("User",back_populates="posts")
    comments=relationship("Comment",back_populates="post")

class Comment(Base):
    id = Column(Integer,primary_key = True, index=True)
    comment=Column(String,nullable= False)
    post_id=Column(Integer,ForeignKey("Post.id"))
    post=relationship("Post",back_populates="comments")
    user_id=Column(Integer,ForeignKey("User.id"))
    user=relationship("User",back_populates="comments")
