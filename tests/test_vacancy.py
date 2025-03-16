import unittest

from src.vacancy import Vacancy  # Предполагая, что файл называется vacancy.py


class TestVacancy(unittest.TestCase):
    """Класс для тестирования функциональности класса Vacancy."""

    def test_initialization(self):
        """Тестирует инициализацию объекта Vacancy. Проверяет, что при создании объекта
        правильно устанавливаются атрибуты title, url, salary и description."""

        vacancy = Vacancy("Программист", "http://example.com", 100000, "Разработка ПО")
        self.assertEqual(vacancy.title, "Программист")
        self.assertEqual(vacancy.url, "http://example.com")
        self.assertEqual(vacancy.salary, "100000")
        self.assertEqual(vacancy.description, "Разработка ПО")

    def test_salary_validation(self):
        """Тестирует валидацию зарплаты. Проверяет, что при передаче отрицательной зарплаты или None
        возвращается сообщение "Зарплата не указана"."""

        vacancy = Vacancy("Программист", "http://example.com", -5000)
        self.assertEqual(vacancy.salary, "Зарплата не указана")

        vacancy = Vacancy("Программист", "http://example.com", None)
        self.assertEqual(vacancy.salary, "Зарплата не указана")

        vacancy = Vacancy("Программист", "http://example.com", 5000)
        self.assertEqual(vacancy.salary, "5000")

    def test_repr(self):
        """Тестирует метод __repr__ объекта Vacancy. Проверяет, что метод возвращает ожидаемую строку
        представления объекта Vacancy."""

        vacancy = Vacancy("Программист", "http://example.com", 100000)
        self.assertEqual(repr(vacancy), "Программист | 100000 | http://example.com")

    def test_str(self):
        """Тестирует метод __str__ объекта Vacancy. Проверяет, что метод возвращает ожидаемую строку
        с информацией о вакансии."""

        vacancy = Vacancy("Программист", "http://example.com", 100000, "Разработка ПО")
        self.assertEqual(
            str(vacancy), "Вакансия: Программист, URL: http://example.com, Зарплата: 100000, Описание: Разработка ПО"
        )

    def test_cast_to_object_list(self):
        """Тестирует метод cast_to_object_list. Проверяет корректную конвертацию списка словарей с данными
        о вакансиях в список объектов класса Vacancy."""

        data = [
            {
                "name": "Программист",
                "alternate_url": "http://example.com/1",
                "salary": {"from": 80000},
                "snippet": {"responsibility": "Разработка ПО"},
            },
            {
                "name": "Аналитик",
                "alternate_url": "http://example.com/2",
                "salary": {"from": 60000},
                "snippet": {"responsibility": "Анализ данных"},
            },
        ]
        vacancies = Vacancy.cast_to_object_list(data)
        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0].title, "Программист")
        self.assertEqual(vacancies[1].title, "Аналитик")


if __name__ == "__main__":
    unittest.main()
