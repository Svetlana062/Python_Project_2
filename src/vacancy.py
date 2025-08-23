from typing import Any, Dict, List, Optional


class Vacancy:
    """Класс для работы с вакансиями."""

    __slots__ = ("title", "url", "salary", "description")

    def __init__(self, title: str, url: str, salary: Optional[float] = None, description: str = ""):
        self.title = title
        self.url = url
        self.salary = self.__validate_salary(salary)  # Используем приватный метод для валидации
        self.description = description

    def to_dict(self):
        """Преобразует объект Vacancy в словарь."""
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description,
        }

    @staticmethod
    def __validate_salary(salary: Optional[float]) -> str:
        """Метод валидации зарплаты"""
        if salary is None or (isinstance(salary, (int, float)) and salary < 0):
            return "Зарплата не указана"  # Возвращаем строку, если зарплата невалидна
        return str(salary)  # Если валидно, возвращаем зарплату как строку

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнивает текущий объект с другим объектом класса Vacancy по значению зарплаты."""
        self_salary = self.salary if isinstance(self.salary, (int, float)) else float("inf")
        other_salary = other.salary if isinstance(other.salary, (int, float)) else float("inf")
        return self_salary < other_salary

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта Vacancy для представления в консоли."""
        return f"{self.title} | {self.salary} | {self.url}"

    def __str__(self) -> str:
        """Строковое представление объекта Vacancy."""
        return f"Вакансия: {self.title}, URL: {self.url}, Зарплата: {self.salary}, Описание: {self.description}"

    @staticmethod
    def cast_to_object_list(data: List[Dict[str, Any]]) -> List["Vacancy"]:
        """Преобразует список словарей с данными о вакансиях в список объектов класса Vacancy."""
        vacancies = []
        for item in data:
            if item is None:
                continue  # Пропустим пустые значения

            title = item.get("name", "Без названия")  # Установим значение по умолчанию, если название отсутствует
            url = item.get("alternate_url", "")  # Значение по умолчанию для URL
            salary_info = item.get("salary")  # Получаем информацию о зарплате
            salary = (
                salary_info["from"] if salary_info and "from" in salary_info else None
            )  # Проверяем существование salary_info

            description = item.get("snippet", {}).get("responsibility", "")
            if description is None:
                description = ""
            vacancies.append(Vacancy(title, url, salary, description))
        return vacancies
