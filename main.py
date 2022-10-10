from fastapi import FastAPI
from db.base import Base
from core.config import engine
from routers.dependencies import include_router

Base.metadata.create_all(bind=engine)

def createTable():
    Base.metadata.create_all(bind=engine)


def start_app():
    app = FastAPI(title='Monolotic Service',version='001')
    createTable()
    include_router(app)
    return app



app=start_app()



@app.get('/')
def Index():
    return 'hello word agan'