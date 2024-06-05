from sqlalchemy.orm import Session
from ..models.user import User as User_model
from ..schemas.user import User, UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int):
    return db.query(User_model).filter(User_model.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User_model).filter(User_model.username == username).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User_model(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
