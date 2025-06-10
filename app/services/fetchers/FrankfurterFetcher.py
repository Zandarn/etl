from datetime import datetime

from sqlalchemy.orm import Session

from app.db.session import get_session
from app.repositories import FrankfurterRepository, CurrencyRepository, RateRepository
from app.services.fetchers import BaseFetcher


class FrankfurterFetcher(BaseFetcher):
    ID: int = 1
    frankfurter_repo: FrankfurterRepository
    currency_repo: CurrencyRepository
    rate_repo: RateRepository

    def __init__(self):
        self.frankfurter_repo = FrankfurterRepository()
        self.currency_repo = CurrencyRepository()
        self.rate_repo = RateRepository()

    def get_rates(self):
        db = next(get_session())
        data = self.frankfurter_repo.fetch_all("cad")
        currencies = self.currency_repo.get_all(db)
        for code, rate in data["rates"].items():
            if code.upper() in currencies.values():
                currency_id = currencies.get(code)
                self.save_rates(db, rate, currency_id)

    def save_rates(self, db: Session, rate, target_currency_id: int) -> None:
        self.rate_repo.create(
            db,
            {
                "fetcher_id": self.ID,
                "base_currency_id": 1,
                "target_currency_id": target_currency_id,
                "rate": rate,
                "fetched_at": datetime.now(),
            },
        )
