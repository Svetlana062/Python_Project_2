class Vacancy:
    """Класс для работы с вакансиями."""

    def __init__(self, title: str, url: str, salary=None, description: str = ""):
        self.title = title
        self.url = url
        self.salary = self.validate_salary(salary)  # Используем статический метод для валидации
        self.description = description

    @staticmethod
    def validate_salary(salary):
        """Метод валидации зарплаты"""
        if salary is None or (isinstance(salary, (int, float)) and salary < 0):
            return "Зарплата не указана"
        return salary

    def __lt__(self, other):
        """Сравнивает текущий объект с другим объектом класса Vacancy по значению зарплаты."""
        return (self.salary if isinstance(self.salary, (int, float)) else float("inf")) < (
            other.salary if isinstance(other.salary, (int, float)) else float("inf")
        )

    def __repr__(self):
        """Возвращает строковое представление объекта Vacancy для представления в консоли."""
        return f"{self.title} | {self.salary} | {self.url}"

    def __str__(self):
        """Строковое представление объекта Vacancy."""
        return f"Вакансия: {self.title}, URL: {self.url}, Зарплата: {self.salary}, Описание: {self.description}"

    @staticmethod
    def cast_to_object_list(data):
        """Преобразует список словарей с данными о вакансиях в список объектов класса Vacancy."""
        vacancies = []
        for item in data:
            if item is None:
                continue  # Пропустим пустые значения

            title = item.get("name")
            url = item.get("alternate_url")
            salary_info = item.get("salary")  # Получаем информацию о зарплате
            salary = salary_info.get("from", None) if salary_info else None  # Проверяем существование salary_info

            description = item.get("snippet", {}).get("responsibility", "")

            vacancies.append(Vacancy(title, url, salary, description))
        return vacancies
