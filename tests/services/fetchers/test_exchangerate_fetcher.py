from datetime import datetime
from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session

from app.repositories import ExchangerateRepository, CurrencyRepository, RateRepository
from app.services.fetchers import ExchangerateFetcher


@pytest.fixture
def db_session():
    return MagicMock(spec=Session)


@pytest.fixture
def exchangerate_fetcher():
    fetcher = ExchangerateFetcher()
    fetcher.exchangerate_repo = MagicMock(spec=ExchangerateRepository)
    fetcher.currency_repo = MagicMock(spec=CurrencyRepository)
    fetcher.rate_repo = MagicMock(spec=RateRepository)
    return fetcher


def test_get_rates(db_session, exchangerate_fetcher):
    expected_fetcher_response = {
        "provider": "https://www.exchangerate-api.com",
        "base": "CAD",
        "date": "2025-05-19",
        "time_last_updated": 1747612801,
        "rates": {"CAD": 1, "USD": 2, "UAH": 4, "ALL": 62.86, "AMD": 276.8, "EUR": 3},
    }
    expected_currencies = {1: "USD", 2: "EUR"}

    exchangerate_fetcher.exchangerate_repo.fetch_all.return_value = (
        expected_fetcher_response
    )
    exchangerate_fetcher.currency_repo.get_all.return_value = expected_currencies

    exchangerate_fetcher.save_rates = MagicMock()
    exchangerate_fetcher.rate_repo.create = MagicMock()

    exchangerate_fetcher.get_rates()
    exchangerate_fetcher.save_rates.call_count = 3


def test_save_rates(exchangerate_fetcher, db_session):
    exchangerate_fetcher.rate_repo.create = MagicMock()

    exchangerate_fetcher.save_rates(db_session, 1, 1)
    exchangerate_fetcher.rate_repo.create.assert_called_once_with(
        db_session,
        {
            "fetcher_id": exchangerate_fetcher.ID,
            "base_currency_id": 1,
            "target_currency_id": 1,
            "rate": 1,
            "fetched_at": datetime.now(),
        },
    )
