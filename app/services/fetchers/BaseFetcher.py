from abc import ABC, abstractmethod


class BaseFetcher(ABC):
    @abstractmethod
    def get_rates(self):
        pass
