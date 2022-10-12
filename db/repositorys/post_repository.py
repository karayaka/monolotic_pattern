from statistics import mode
from turtle import tilt
from sqlalchemy.orm import Session
from db.models.post import Post
from db.models.user import User
from schemas.posts import PostCreate

def get_all_posts(db:Session,user_id:int):
    return db.query(Post).filter(Post.user_id==user_id).all()

def create_new_post(db:Session,model:Post):
    
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

        