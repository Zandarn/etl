import redis
from redis.backoff import ExponentialBackoff

from redis.retry import Retry

from redis.client import Redis

from redis.exceptions import BusyLoadingError, ConnectionError, TimeoutError
from app.core.config import settings

retry = Retry(ExponentialBackoff(), 3)
redis_client = redis.Redis(
    host=settings.redis_url,
    port=settings.redis_port,
    db=settings.redis_db,
    decode_responses=True,
    retry=retry,
    retry_on_error=[BusyLoadingError, ConnectionError, TimeoutError],
)
