import requests

from abstract_class_api import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """Класс для работы с вакансиями"""

    BASE_URL = "https://api.hh.ru/vacancies"

    def connect(self):
        """Метод для тестирования подключения (проверка доступности API)."""
        response = requests.get(self.BASE_URL)
        if response.status_code != 200:
            raise Exception("Соединение не удалось.")
        return response

    def get_vacancies(self, keyword: str, per_page: int = 20):
        """Метод для получения вакансий."""
        params = {
            "text": keyword,
            "per_page": per_page,  # аргумент, который определяет, сколько вакансий API должен вернуть в одном запросе
        }
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()["items"]
        else:
            raise Exception("Не удалось получить вакансии.")
