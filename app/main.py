from fastapi import FastAPI

from app.db.session import engine
from app.models.base import Base
from app.models.user import User
from app.api import router


app = FastAPI(title="Iticket API")
app.include_router(router)

Base.metadata.create_all(engine)


@app.get("/")
async def root_view():
    return {"message": "project is running..."}
