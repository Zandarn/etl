from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Fetcher(Base):
    __tablename__ = "fetchers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
