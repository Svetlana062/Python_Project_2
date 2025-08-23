import unittest
from unittest.mock import patch

from src.hhru_api import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        """Создает экземпляр HeadHunterAPI перед каждым тестом."""
        self.api = HeadHunterAPI()

    @patch("src.hhru_api.requests.get")
    def test_connect_success(self, mock_get):
        """Тестирование успешного соединения с API."""
        mock_get.return_value.status_code = 200

        # Вызываем метод соединения
        self.api._connect()

        # Проверяем, что соединение установлено
        self.assertTrue(hasattr(self.api, "_HeadHunterAPI__is_connected"))
        self.assertTrue(self.api._HeadHunterAPI__is_connected)

    @patch("src.hhru_api.requests.get")
    def test_connect_failure(self, mock_get):
        """Тестирование неудачного соединения с API."""
        mock_get.return_value.status_code = 404  # имитируем ошибку

        with self.assertRaises(Exception) as context:
            self.api._connect()

        self.assertTrue("Соединение не удалось." in str(context.exception))

    @patch("src.hhru_api.requests.get")
    def test_get_vacancies_success(self, mock_get):
        """Тестирование успешного получения вакансий."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "items": [{"id": 1, "name": "Вакансия 1"}, {"id": 2, "name": "Вакансия 2"}]
        }

        result = self.api.get_vacancies("developer", per_page=2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Вакансия 1")
        self.assertEqual(result[1]["name"], "Вакансия 2")


if __name__ == "__main__":
    unittest.main()
