from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session

from app.models import Fetcher
from app.repositories import FetcherRepository


@pytest.fixture
def db_session():
    return MagicMock(spec=Session)


@pytest.fixture
def fetcher_repository():
    return FetcherRepository()


def test_fetch_all(fetcher_repository, db_session):
    expected_result = Fetcher(id=1, name="mock")
    db_session.query.return_value.all.return_value = [expected_result]

    result = fetcher_repository.get_all(db_session)
    db_session.query.assert_called_once_with(Fetcher)
    assert len(result) == 1
    assert result[0] == expected_result


def test_fetch_by_id(fetcher_repository, db_session):
    expected_result = Fetcher(id=1, name="mock")
    db_session.query.return_value.filter.return_value.first.return_value = (
        expected_result
    )

    result = fetcher_repository.get_by_id(db_session, 1)
    db_session.query.assert_called_once_with(Fetcher)
    assert result == expected_result
