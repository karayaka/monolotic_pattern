from pydantic import BaseModel

class BaseItem(BaseModel):
    id :int
    name:str
    desc:str

    
class ItemList(BaseModel):
    user_name_surname:str
