from unittest.mock import patch

import pytest

from app.repositories import FrankfurterRepository


@pytest.fixture
def frankfurter_repository():
    return FrankfurterRepository()


@patch("app.repositories.frankfurter_repository.requests.get")
def test_fetch_all(mock_get, frankfurter_repository):
    expected_response = {
        "amount": 1.0,
        "base": "CAD",
        "date": "2025-05-16",
        "rates": {"EUR": 0.63939, "USD": 0.71573},
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = expected_response

    result = frankfurter_repository.fetch_all("cad")
    assert result == expected_response


@patch("app.repositories.frankfurter_repository.requests.get")
def test_fetch_all_404(mock_get, frankfurter_repository):
    expected_response = {}

    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = expected_response

    result = frankfurter_repository.fetch_all("cad")
    assert result == expected_response
