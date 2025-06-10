from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_session
from app.services import CurrencyService, RatesService
from app.services.fetchers import ExchangerateFetcher

router = APIRouter()


@router.get("/ping", tags=["health"])
def ping():
    return {"status": "ok", "version": settings.api_version}


@router.get("/run")
def run_fetcher():
    return ExchangerateFetcher().get_rates()


@router.get("/banks/{bank_id}/rates")
def bank_rates(session: Session = Depends(get_session), bank_id: int = 1):
    return RatesService().get_rates(session, bank_id)


@router.get("/currencies")
def rates(session: Session = Depends(get_session)):
    return CurrencyService().get_all(session)
