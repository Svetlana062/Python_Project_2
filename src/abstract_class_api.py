from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass
