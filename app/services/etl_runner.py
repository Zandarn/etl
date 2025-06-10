import importlib

from app.db.session import get_session
from app.services.fetchers import BaseFetcher


def execute_fetcher(fetcher: BaseFetcher):
    session_gen = get_session()
    session = next(session_gen)

    try:
        fetcher.get_rates()

        session.commit()
    except Exception as e:
        print(f"ETL error: {e}")
        session.rollback()
    finally:
        session.close()


def get_fetchers_classes(package_name: str):
    package = importlib.import_module(package_name)

    fetchers_classes = {}
    for module_name in dir(package):
        module = getattr(package, module_name)

        if (
            isinstance(module, type)
            and issubclass(module, BaseFetcher)
            and module is not BaseFetcher
        ):
            fetchers_classes[module_name] = module

    return fetchers_classes


if __name__ == "__main__":
    fetchers = get_fetchers_classes("app.services.fetchers")

    for name, f in fetchers.items():
        print(f"Found fetcher class: {name}")
        execute_fetcher(f())
