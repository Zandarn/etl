import requests

from app.core.config import settings


class ExchangerateRepository:
    base_url: str

    def __init__(self):
        self.base_url = settings.exchangerate_url

    def fetch_all(self, base_currency: str):
        url = self.base_url + "/" + base_currency
        response = requests.get(url)
        if response.status_code != 200:
            return {}

        return response.json()
