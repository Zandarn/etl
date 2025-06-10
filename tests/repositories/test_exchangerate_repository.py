from unittest.mock import patch

import pytest

from app.repositories import ExchangerateRepository


@pytest.fixture
def exchangerate_repository():
    return ExchangerateRepository()


@patch("app.repositories.exchangerate_repository.requests.get")
def test_fetch_all(mock_get, exchangerate_repository):
    expected_response = {
        "provider": "https://www.exchangerate-api.com",
        "base": "CAD",
        "date": "2025-05-19",
        "time_last_updated": 1747612801,
        "rates": {
            "CAD": 1,
            "AED": 2.63,
            "AFN": 50.16,
            "ALL": 62.86,
            "AMD": 276.8,
            "ANG": 1.28,
        },
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = expected_response

    result = exchangerate_repository.fetch_all("cad")
    assert result == expected_response


@patch("app.repositories.exchangerate_repository.requests.get")
def test_fetch_all_404(mock_get, exchangerate_repository):
    expected_response = {}

    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = expected_response

    result = exchangerate_repository.fetch_all("cad")
    assert result == expected_response
