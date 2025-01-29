from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


class UserDetail(BaseModel):
    name: str
    age: int
    email: str
    phone: str