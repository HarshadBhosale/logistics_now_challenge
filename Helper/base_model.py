from peewee import Model
from .database import database


class BaseModel(Model):
    class Meta:
        database = database
