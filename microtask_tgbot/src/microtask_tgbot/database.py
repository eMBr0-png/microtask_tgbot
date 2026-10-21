# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import String, BigInteger, DateTime, func, Text
# from config import settings

# engine = create_async_engine(settings.database_url, echo=False)
# session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# class Base(DeclarativeBase):
#     pass

# class Task(Base):
#     __tablename__ = "task"

#     user_id: Mapped[int] = mapped_column(BigInteger, index=True)
#     text: Mapped[str] = mapped_column(Text)
#     created_at: Mapped[DateTime] = mapped_column(DataTime(timezone=True), server_default=func.now())

# # class Statistic(Base):
# #     __tablename__ = "statistic"

# #     user_id: Mapped[int] = mapped_column(BigInteger, index=True)
    


# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)