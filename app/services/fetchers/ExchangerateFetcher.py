from datetime import datetime

from sqlalchemy.orm import Session

from app.db.session import get_session
from app.repositories import ExchangerateRepository, CurrencyRepository, RateRepository
from app.services.fetchers import BaseFetcher


class ExchangerateFetcher(BaseFetcher):
    ID: int = 2
    exchange_repo: ExchangerateRepository
    currency_repo: CurrencyRepository
    rate_repo: RateRepository

    def __init__(self):
        self.exchangerate_repo = ExchangerateRepository()
        self.currency_repo = CurrencyRepository()
        self.rate_repo = RateRepository()

    def get_rates(self):
        db = next(get_session())
        data = self.exchangerate_repo.fetch_all("cad")
        currencies = self.currency_repo.get_all(db)
        for code, rate in data["rates"].items():
            if code.upper() in currencies.values():
                currency_id = currencies.get(code.upper())
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
