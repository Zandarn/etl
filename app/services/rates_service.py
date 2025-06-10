from sqlalchemy.orm import Session

from app.repositories import FetcherRepository, RateRepository, CurrencyRepository


class RatesService:
    fetcher_repo: FetcherRepository
    currency_repo: CurrencyRepository
    rate_repo: RateRepository

    def __init__(self):
        self.fetcher_repo = FetcherRepository()
        self.currency_repo = CurrencyRepository()
        self.rate_repo = RateRepository()

    def get_rates(self, db: Session, bank_id: int) -> list:
        currencies = self.currency_repo.get_all(db)
        fetcher = self.fetcher_repo.get_by_id(db, bank_id)
        if fetcher is None:
            return []

        rates = self.rate_repo.get_by_fetcher_id(db, fetcher.id)
        cross_rates = self.calculate_cross_rates(currencies, rates)

        return cross_rates

    def calculate_cross_rates(self, currencies, rates: list) -> list:
        cross_rates = []

        index = {(r.base_currency_id, r.target_currency_id): r.rate for r in rates}
        fetched_at_map = {
            (r.base_currency_id, r.target_currency_id): r.fetched_at for r in rates
        }
        currencies_map = set(
            sum(([r.base_currency_id, r.target_currency_id] for r in rates), [])
        )

        for currency_base in currencies_map:
            for currency_target in currencies_map:
                if currency_base == currency_target:
                    continue

                for common in currencies_map:
                    try:
                        r1 = index[(common, currency_base)]
                        r2 = index[(common, currency_target)]
                        fetched1 = fetched_at_map[(common, currency_base)]
                        fetched2 = fetched_at_map[(common, currency_target)]
                        fetched_at = max(fetched1, fetched2)
                        cross_rates.append(
                            {
                                "base_currency": currencies.get(currency_base),
                                "target_currency": currencies.get(currency_target),
                                "rate": r2 / r1,
                                "fetched_at": fetched_at,
                            }
                        )
                        break
                    except KeyError:
                        continue

        cross_rates.extend(
            [
                {
                    "base_currency": currencies.get(r.base_currency_id),
                    "target_currency": currencies.get(r.target_currency_id),
                    "rate": r.rate,
                    "fetched_at": r.fetched_at,
                }
                for r in rates
            ]
        )

        return cross_rates
