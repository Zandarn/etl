from typing import Union

from sqlalchemy.orm import Session

from app.models import Fetcher


class FetcherRepository:
    def get_all(self, db: Session) -> Union[dict, list]:
        return db.query(Fetcher).all()

    def get_by_id(self, db: Session, bank_id: int):
        return db.query(Fetcher).filter(Fetcher.id == bank_id).first()
