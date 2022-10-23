from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from schemas.users import TokenData
from schemas.posts import PostCreate,PostList
from core.aut2Hadler import get_current_user
from core.config import get_db
from db.models.post import Post
from db.repositorys.post_repositoryinj import PostRepository
from db.repositorys.post_repository import get_all_posts,create_new_post

router=APIRouter(
    prefix='/posts',
    tags=['Posts']    
)

@router.get('/')
def get_posts(db:Session =Depends(get_db),current_user:TokenData=Depends(get_current_user)):
    posts=get_all_posts(db=db,user_id=current_user.id)
    return posts
#post create update delete yazıalcak sonrda özel sorgualara geçilecek
@router.post('/')
def create_post(model:PostCreate, db:Session =Depends(get_db),current_user:TokenData=Depends(get_current_user)):
    post=Post()
    post.title=model.title
    post.content=model.content
    post.user_id=current_user.id
    return create_new_post(db=db,model=post)
# fast api için repository yapısı kurgusu yapıldı sırada generick yapılar var
@router.get('/all')
def get_all_post(rep:PostRepository=Depends()):
    return rep.get_all_post()


