from fastapi import Depends
from sqlalchemy.orm import Session
from core.config import get_db
from db.models.post import Post

class PostRepository():

    def __init__(self,db:Session=Depends(get_db)) -> None:
        self.db=db


    def get_all_post(self):
        #cllass içinden değişkenklere nasıl erişiliyor
        return self.db.query(Post).all()