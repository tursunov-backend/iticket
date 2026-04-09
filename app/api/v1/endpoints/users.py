from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/")
async def users_view():
    pass


@router.get("/{id}")
async def get_user_view(id: int):
    pass


@router.patch("/{id}")
async def update_user_view(id):
    pass
