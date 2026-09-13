# This file is for connection with the database.
#  ----------- This is for synchronous code -----------------
# from sqlalchemy import create_engine
# from sqlalchemy.orm import DeclarativeBase, sessionmaker


# ----------- for asynchronous code -------------
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase 

# This is the file name that gets created automatically when the connection is build
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"

# engine is the connection ot the db - not immediately , it does it lazily.
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread" : False}

)

# creates db sessions - a session is basically a transaction 
# with the database.
# autocommit and autoflush is equal to false, because we want to control when changes are commited.

# SessionLocal is a session factory

#  ------------ for sync code --------
# SessionLocal = sessionmaker(autocommit = False , autoflush=False, bind=engine)


# ------------- for async code -------------
AsyncSessionLocal =  async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    pass

async def get_db():
    # with act as a context manager - whe  the block finishes , it closes the session automatically.
    # this is dependency function that gives independent sessions to our routes 
    async with AsyncSessionLocal() as session:
        yield session
