import json
import os
from typing import List

from .abstract_file_handler import AbstractFileHandler


class JSONFileHandler(AbstractFileHandler):
    """Создать класс для сохранения информации о вакансиях в JSON-файл."""

    def __init__(self, filename: str = "data/vacancies.json"):
        self._filename = filename  # имя файла

    def load(self) -> List[dict]:
        """Загружает данные из файла JSON."""

        if os.path.exists(self._filename):
            try:
                with open(self._filename, "r", encoding="utf-8") as file:
                    return json.load(file)
            except json.JSONDecodeError:  # Обработка ошибки загрузки JSON
                return []
        return []

    def save(self, data) -> None:
        """Сохраняет данные в файл JSON."""

        existing_data = self.load()
        existing_data.append(data)
        try:
            with open(self._filename, "w", encoding="utf-8") as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
        except Exception as e:  # Обработка любых других ошибок записи
            print(f"Ошибка при сохранении данных: {e}")

    def delete(self, data) -> None:
        """Удаляет данные из файла JSON."""

        existing_data = self.load()
        if data in existing_data:
            existing_data.remove(data)
            try:
                with open(self._filename, "w", encoding="utf-8") as file:
                    json.dump(existing_data, file, ensure_ascii=False, indent=4)
            except Exception as e:
                print(f"Ошибка при удалении данных: {e}")
