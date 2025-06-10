from typing import Union

import requests

from app.core.config import settings


class FrankfurterRepository:
    base_url: str

    def __init__(self):
        self.base_url = settings.frankfurter_url

    def fetch_all(self, base_currency: str) -> Union[dict, list]:
        url = self.base_url + "?base=" + base_currency + "&symbols=USD,UAH,EUR"
        response = requests.get(url)
        if response.status_code != 200:
            return {}

        return response.json()
