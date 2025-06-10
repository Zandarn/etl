# tests/services/test_rates_service.py
from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session

from app.services.rates_service import RatesService


@pytest.fixture
def db_session():
    return MagicMock(spec=Session)


@pytest.fixture
def rates_service():
    return RatesService()


def test_get_rates_no_fetcher(db_session, rates_service):
    rates_service.currency_repo.get_all = MagicMock(return_value=[])
    rates_service.fetcher_repo.get_by_id = MagicMock(return_value=None)
    result = rates_service.get_rates(db_session, bank_id=1)
    assert result == []
    rates_service.fetcher_repo.get_by_id.assert_called_once_with(db_session, 1)


def test_get_rates_with_valid_fetcher(db_session, rates_service):
    currencies = '{"1": "USD", "2": "EUR"}'
    fetcher = MagicMock(id=123)
    rates = [
        MagicMock(
            base_currency_id=1,
            target_currency_id=2,
            rate=1.123,
            fetched_at="2020-10-10",
        )
    ]

    rates_service.currency_repo.get_all = MagicMock(return_value=currencies)
    rates_service.fetcher_repo.get_by_id = MagicMock(return_value=fetcher)
    rates_service.rate_repo.get_by_fetcher_id = MagicMock(return_value=rates)
    rates_service.calculate_cross_rates = MagicMock(return_value=[])

    result = rates_service.get_rates(db_session, bank_id=123)

    rates_service.currency_repo.get_all.assert_called_once_with(db_session)
    rates_service.fetcher_repo.get_by_id.assert_called_once_with(db_session, 123)
    rates_service.rate_repo.get_by_fetcher_id.assert_called_once_with(
        db_session, fetcher.id
    )

    assert result == []


def test_calculate_cross_rates_empty_input(rates_service):
    currencies = {}
    rates = []

    result = rates_service.calculate_cross_rates(currencies, rates)
    assert result == []


def test_calculate_cross_rates_with_data(rates_service):
    currencies = {1: "USD", 2: "EUR", 3: "UAH"}
    rates = [
        MagicMock(
            base_currency_id=1,
            target_currency_id=2,
            rate=1.123,
            fetched_at="2023-10-10",
        ),
        MagicMock(
            base_currency_id=1,
            target_currency_id=3,
            rate=1.345,
            fetched_at="2023-10-09",
        ),
        MagicMock(
            base_currency_id=2,
            target_currency_id=3,
            rate=0.567,
            fetched_at="2023-10-08",
        ),
    ]

    result = rates_service.calculate_cross_rates(currencies, rates)

    assert len(result) > 0
    for r in result:
        assert "base_currency" in r
        assert "target_currency" in r
        assert "rate" in r
        assert "fetched_at" in r
