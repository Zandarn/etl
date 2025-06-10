from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session

from app.repositories import FrankfurterRepository, CurrencyRepository, RateRepository
from app.services.fetchers import FrankfurterFetcher


@pytest.fixture
def db_session():
    return MagicMock(spec=Session)


@pytest.fixture
def frankfurter_fetcher():
    fetcher = FrankfurterFetcher()
    fetcher.frankfurter_repo = MagicMock(spec=FrankfurterRepository)
    fetcher.currency_repo = MagicMock(spec=CurrencyRepository)
    fetcher.rate_repo = MagicMock(spec=RateRepository)
    return fetcher


def test_get_rates(db_session, frankfurter_fetcher):
    expected_fetcher_response = {
        "amount": 1.0,
        "base": "CAD",
        "date": "2025-05-16",
        "rates": {"ABC": 0.63939, "USD": 0.71573},
    }
    expected_currencies = {1: "USD", 2: "EUR", 3: "UAH"}

    frankfurter_fetcher.frankfurter_repo.fetch_all.return_value = (
        expected_fetcher_response
    )
    frankfurter_fetcher.currency_repo.get_all.return_value = expected_currencies

    frankfurter_fetcher.rate_repo.create = MagicMock()
    frankfurter_fetcher.get_rates()
