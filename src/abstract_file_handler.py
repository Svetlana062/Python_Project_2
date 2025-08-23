from abc import ABC, abstractmethod
from typing import Any, List


class AbstractFileHandler(ABC):
    """Абстрактный класс для работы с данными: получение,
    сохранение, удаление."""

    @abstractmethod
    def load(self) -> List[dict]:
        """Метод предназначен для загрузки данных."""
        pass

    @abstractmethod
    def save(self, data: dict) -> None:
        """Метод предназначен для сохранения данных."""
        pass

    @abstractmethod
    def delete(self, data: Any) -> None:
        """Метод предназначен для удаления информации о вакансиях."""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Метод предназначен для очистки данных"""
        pass
