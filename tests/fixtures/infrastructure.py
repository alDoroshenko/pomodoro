import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.settings import Settings

from app.infrastructure.database.database import Base

engine = create_async_engine(url="postgresql+asyncpg://postgres:postgres@localhost:5435/pomodoro", future=True,
                             echo=True, pool_pre_ping=True)


@pytest.fixture()
def settings():
    return Settings()


AsyncSessionFactory = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)


@pytest_asyncio.fixture(scope="session", autouse=True)
async def init_models(event_loop):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def get_db_session() -> AsyncSession:
   yield AsyncSessionFactory()
   await AsyncSessionFactory().close_all()
