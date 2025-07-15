import os
import asyncio
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import find_dotenv, load_dotenv
find_dotenv(load_dotenv)

engine = create_async_engine(url=os.getenv('DATABASE_URL'))
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    usr_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(32), nullable=True)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_db())