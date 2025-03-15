from abc import ABC, abstractmethod


class AbstractFileHandler(ABC):

    @abstractmethod
    def load(self):
        """Метод предназначен для загрузки данных."""
        pass

    @abstractmethod
    def save(self, data):
        """Метод предназначен для сохранения данных."""
        pass

    @abstractmethod
    def delete(self, data):
        """Метод предназначен для удаления информации о вакансиях."""
        pass
