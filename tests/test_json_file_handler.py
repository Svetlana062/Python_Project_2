import os
import unittest

from src.json_file_handler import JSONFileHandler  # Убедитесь, что это правильный импорт вашего файла


class TestJSONFileHandler(unittest.TestCase):
    def setUp(self):
        """Создаем экземпляр JSONFileHandler с временным именем файла перед каждым тестом."""
        self.file_handler = JSONFileHandler(filename="test_vacancies.json")

    def tearDown(self):
        """Удаляем временный файл после каждого теста, если он существует."""
        if os.path.exists("test_vacancies.json"):
            os.remove("test_vacancies.json")

    def test_load_empty_file(self):
        """Тестирует метод load, когда файл не существует - должен вернуть пустой список."""
        result = self.file_handler.load()
        self.assertEqual(result, [])

    def test_save_and_load(self):
        """Тестирует сохранение данных и последующую их загрузку."""
        data = {"title": "Программист", "salary": 100000}
        self.file_handler.save(data)
        result = self.file_handler.load()
        self.assertIn(data, result)

    def test_delete(self):
        """Тестирует удаление данных из файла."""
        data = {"title": "Программист", "salary": 100000}
        self.file_handler.save(data)
        self.file_handler.delete(data)
        result = self.file_handler.load()
        self.assertNotIn(data, result)


if __name__ == "__main__":
    unittest.main()
