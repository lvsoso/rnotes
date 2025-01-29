from fastapi import APIRouter
from routers.api_v1.schemas.user import User,UserDetail

router = APIRouter()

fake_db = [
    UserDetail(name="1", age=33, email='', phone=''),
    UserDetail(name="2", age=44, email='', phone='')
]

@router.get("/")
async def get_users() -> list[User]:
    return [User(u.dict()) for u in fake_db]

@router.get("/extras", response_model=list[UserDetail])
async def get_users_extras() -> list[UserDetail]:
    return fake_db

@router.get("/{user_id}", summary="Get a user", description="Get a user")
async def get_user(user_id: str) -> User:
    """
    # Markdown
    ## Get User

    - get user name
    - get user ID
    """
    return User(fake_db[int(user_id)].dict())

@router.post("/", summary="Create a user", description="Create a user")
async def create_user(user: User) -> User:
    return user
