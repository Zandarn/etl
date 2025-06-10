from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session

from app.services.currency_service import CurrencyService


@pytest.fixture
def db_session():
    return MagicMock(spec=Session)


@pytest.fixture
def currency_service():
    return CurrencyService()


def test_get_all(db_session, currency_service):
    currencies = [MagicMock(id=1, code="USD"), MagicMock(id=2, code="EUR")]
    currency_service.currency_repo.get_all = MagicMock(return_value=currencies)
    result = currency_service.get_all(db_session)
    assert result == currencies
    currency_service.currency_repo.get_all.assert_called_once_with(db_session)
