import fastapi
from Helper.user import user_router
from Helper.database import database
from Helper.create_default_table import create_not_existence_tables
from fastapi.middleware.cors import CORSMiddleware


api = fastapi.FastAPI()


origins = [
    "*",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)


@api.on_event("startup")
def startup_event():
    if database.is_closed():
        database.connect()
    create_not_existence_tables()


@api.on_event("shutdown")
def shutdown_event():
    if not database.is_closed():
        database.close()


@api.get("/")
def root():
    return {"VERSION": "1.0.0"}


api.include_router(user_router)
