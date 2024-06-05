from fastapi import FastAPI
from app.database import engine, Base
from app.api import user, token

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(token.router)
