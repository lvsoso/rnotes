from typing import Generator
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core.config import settings
from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db)
) -> models.User:
    user = crud.user.get(db, id=1)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user