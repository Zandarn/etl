from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session

from app.models import CurrencyRate
from app.repositories import RateRepository


@pytest.fixture
def db_session():
    return MagicMock(spec=Session)


@pytest.fixture
def rate_repository():
    return RateRepository()


def test_get_by_fetcher_id(db_session, rate_repository):
    expected_result = CurrencyRate(
        id=1,
        fetcher_id=1,
        base_currency_id=1,
        target_currency_id=2,
        rate=1.123,
        fetched_at="2020-10-10",
    )
    db_session.query.return_value.filter.return_value.all.return_value = [
        expected_result
    ]

    result = rate_repository.get_by_fetcher_id(db_session, bank_id=1)
    db_session.query.assert_called_once_with(CurrencyRate)

    assert len(result) == 1
    assert result[0] == expected_result


def test_create(db_session, rate_repository):
    data = {
        "fetcher_id": 1,
        "base_currency_id": 1,
        "target_currency_id": 2,
        "rate": 1.123,
        "fetched_at": "2020-10-10",
    }

    rate_repository.create(db_session, data)
    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
