from fastapi import FastAPI
import uvicorn
import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# ''' FastAPI CONFIGURATION '''
# app = FastAPI(__name__,
#               title="FastAPI CRUD Example",
#               docs_url="/docs", redoc_url="/redocs"
# )


app = FastAPI()

''' DATABASE CONNECTION '''
DATABASE_URL = "postgresql://postgres:123456789@localhost/posts"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)

Base = declarative_base()


''' APP EVENT SETTING'''
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()