from sqlalchemy.orm import Session

from app.repositories import CurrencyRepository


class CurrencyService:
    currency_repo: CurrencyRepository

    def __init__(self):
        self.currency_repo = CurrencyRepository()

    def get_all(self, db: Session):
        return self.currency_repo.get_all(db)
