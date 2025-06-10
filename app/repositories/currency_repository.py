import json
from sqlalchemy.orm import Session

from app.db.redis import redis_client
from app.models import Currency


class CurrencyRepository:
    CACHE_KEY = "currency"

    def get_all(self, db: Session) -> dict:
        value = redis_client.get(self.CACHE_KEY)
        if value is None or value == {}:
            data = db.query(Currency).all()
            data = {currency.id: currency.code.upper() for currency in data}
            redis_client.set(self.CACHE_KEY, json.dumps(data), 3600)
            return data
        else:
            data = json.loads(value)
            return {int(k): v for k, v in data.items()}
