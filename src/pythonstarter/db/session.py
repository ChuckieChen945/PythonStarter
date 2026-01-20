from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from pythonstarter.component.config_manager import settings

postgre_engine = create_async_engine(
    str(settings.database.postgres_uri),
    future=True,
    pool_size=5,
    max_overflow=10,
    pool_recycle=3600,
    pool_pre_ping=True,
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(postgre_engine, expire_on_commit=False)
