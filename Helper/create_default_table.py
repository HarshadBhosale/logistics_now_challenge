from .base_model import BaseModel
from .database import database


def create_not_existence_tables():
    for table in BaseModel.__subclasses__():
        if not database.table_exists(table.__name__):
            table.create_table()
