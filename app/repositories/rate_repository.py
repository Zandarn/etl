from sqlalchemy.orm import Session

from app.models import CurrencyRate


class RateRepository:
    def get_by_fetcher_id(self, db: Session, bank_id: int) -> list:
        return db.query(CurrencyRate).filter(CurrencyRate.fetcher_id == bank_id).all()

    def create(self, db: Session, params: dict) -> None:
        obj = CurrencyRate(
            fetcher_id=params["fetcher_id"],
            base_currency_id=params["base_currency_id"],
            target_currency_id=params["target_currency_id"],
            rate=params["rate"],
            fetched_at=params["fetched_at"],
        )
        db.add(obj)
        db.commit()
