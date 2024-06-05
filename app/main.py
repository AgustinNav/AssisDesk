from fastapi import FastAPI
from database import engine, Base
from api import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
