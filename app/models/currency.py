from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)
