from datetime import datetime

from sqlalchemy import Column, Integer, BigInteger, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship

from app.db.base import Base


class CurrencyRate(Base):
    __tablename__ = "currency_rates"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    fetcher_id = Column(Integer, ForeignKey("fetchers.id"), nullable=False)
    base_currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    target_currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    rate = Column(Numeric(18, 10), nullable=False)
    fetched_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    # created_at = Column(DateTime, nullable=True, default=datetime.utcnow())

    base_currency = relationship("Currency", foreign_keys=[base_currency_id])
    target_currency = relationship("Currency", foreign_keys=[target_currency_id])
