from Helper.env import envVars
from peewee import PostgresqlDatabase

database = PostgresqlDatabase(
    envVars.DATABASE_NAME,
    user=envVars.DATABASE_USER,
    password=envVars.DATABASE_PASSWORD,
    host=envVars.DATABASE_HOST,
    port=envVars.DATABASE_PORT,
    autorollback=True,
)
