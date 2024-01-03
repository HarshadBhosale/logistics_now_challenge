import peewee
from .base_model import BaseModel as dbBaseModel
from pydantic import BaseModel, constr
from uuid import uuid4, UUID
from datetime import datetime


class Users(dbBaseModel):
    id = peewee.UUIDField(unique=True, default=uuid4)
    name = peewee.CharField()
    username = peewee.CharField(unique=True)
    status = peewee.SmallIntegerField(default=1)
    created_at = peewee.DateTimeField(default=datetime.utcnow())
    updated_at = peewee.DateTimeField(default=datetime.utcnow())


class UserCreateModel(BaseModel):
    name: constr(min_length=1, max_length=255)
    username: constr(min_length=1, max_length=16)


class UserResponseModel(BaseModel):
    id: UUID
    name: str
    username: str
    status: int
