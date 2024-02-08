import fastapi
from .users import UserResponseModel, Users, UserCreateModel
from uuid import UUID
from typing import Optional

user_router = fastapi.APIRouter(prefix="/users")


@user_router.get(
    "/{id}",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=Optional[UserResponseModel],
)
def get_user(id: UUID):
    user = Users.select().where(Users.id == id).get()
    if user.status == 0:
        raise fastapi.HTTPException(
            fastapi.status.HTTP_400_BAD_REQUEST, "User is Deleted"
        )
    return Users.select().where(Users.id == id, Users.status == 1).dicts().get()


@user_router.post(
    "/",
    status_code=fastapi.status.HTTP_201_CREATED,
    response_model=Optional[UserResponseModel],
)
def create_user(user: UserCreateModel):
    if user_exists := Users.select().where(Users.username == user.username):
        raise fastapi.HTTPException(
            fastapi.status.HTTP_400_BAD_REQUEST, "Username already exists"
        )
    user = Users.create(**dict(user))
    return Users.select().where(Users.username == user.username).dicts().get()


@user_router.delete("/{id}", status_code=fastapi.status.HTTP_204_NO_CONTENT)
def delete_user(id: UUID):
    user = Users.select().where(Users.id == id).get()
    if user.status == 0:
        raise fastapi.HTTPException(
            fastapi.status.HTTP_400_BAD_REQUEST, "User is Already Deleted"
        )
    return Users.update(status=0).where(Users.id == id, Users.status == 1).execute()
