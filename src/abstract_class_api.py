from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def _connect(self):
        """Метод для проверки подключения через API."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        """Метод для получения информации через API."""
        pass
