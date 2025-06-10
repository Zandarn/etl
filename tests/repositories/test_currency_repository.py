from unittest.mock import MagicMock, patch

import pytest
from sqlalchemy.orm import Session

from app.repositories.currency_repository import CurrencyRepository


@pytest.fixture
def db_session():
    return MagicMock(spec=Session)


@pytest.fixture
def currency_repository():
    return CurrencyRepository()


@patch("app.repositories.currency_repository.redis_client")
def test_get_all_with_empty_cache(redis_client_mock, db_session, currency_repository):
    db_session.query.return_value.all.return_value = [
        MagicMock(id=1, code="CAD"),
        MagicMock(id=2, code="USD"),
    ]

    currency_repository.redis_client = redis_client_mock
    redis_client_mock.get.return_value = None

    result = currency_repository.get_all(db_session)

    assert result == {1: "CAD", 2: "USD"}
    db_session.query.assert_called_once()
    redis_client_mock.set.assert_called_once()


@patch("app.repositories.currency_repository.redis_client")
def test_get_all_with_cache(redis_client_mock, db_session, currency_repository):
    currency_repository.redis_client = redis_client_mock
    redis_client_mock.get.return_value = '{"1": "USD", "2": "EUR"}'

    result = currency_repository.get_all(db_session)

    assert result == {1: "USD", 2: "EUR"}
    redis_client_mock.get.assert_called_once()
    db_session.query.assert_not_called()
