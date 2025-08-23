import json
import os
from typing import Any, Dict, List

from src.abstract_file_handler import AbstractFileHandler


class JSONFileHandler(AbstractFileHandler):
    """Класс для работы с данными о вакансиях в формате JSON."""

    def __init__(self, filename: str = "../data/vacancies.json"):
        self.__filename = filename  # приватное имя файла для хранения данных

    def load(self) -> List[Dict[str, Any]]:
        """Загружает данные из файла JSON."""
        if os.path.exists(self.__filename):
            try:
                with open(self.__filename, "r", encoding="utf-8") as file:
                    return json.load(file)
            except json.JSONDecodeError:  # Обработка ошибки загрузки JSON
                return []
        return []

    def save(self, data: Dict[str, Any]) -> None:
        """Сохраняет данные в файл JSON."""
        existing_data = self.load()
        if data not in existing_data:  # Проверка на уникальность данных
            existing_data.append(data)
        try:
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
        except Exception as e:  # Обработка любых других ошибок записи
            print(f"Ошибка при сохранении данных: {e}")

    def delete(self, data: Dict[str, Any]) -> None:
        """Удаляет данные из файла JSON."""
        existing_data = self.load()
        if data in existing_data:
            existing_data.remove(data)
            try:
                with open(self.__filename, "w", encoding="utf-8") as file:
                    json.dump(existing_data, file, ensure_ascii=False, indent=4)
            except Exception as e:
                print(f"Ошибка при удалении данных: {e}")

    def clear(self) -> None:
        """Очищает все данные из файла JSON."""
        try:
            with open(self.__filename, "w", encoding="utf-8") as file:
                file.write("[]")  # Запись пустого списка в файл
        except Exception as e:
            print(f"Ошибка при очистке данных: {e}")


if __name__ == "__main__":
    handler = JSONFileHandler()
    sample_data = {"title": "Программист", "salary": 60000}

    # Сохранение данных
    handler.save(sample_data)
    print("Данные успешно сохранены.")
