from src.hhru_api import HeadHunterAPI
from src.json_file_handler import JSONFileHandler  # Импорт обработчика файлов
from src.vacancy import Vacancy


def get_positive_integer(prompt, max_attempts=10):
    """Эта функция запрашивает у пользователя ввод числа и проверяет,
    что оно положительное и является целым числом."""
    attempts = 0
    while attempts < max_attempts:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Количество должно быть положительным целым числом. Попробуйте снова.")
                attempts += 1
                continue
            return value
        except ValueError:
            print("Ошибка: введите корректное целое число.")

    print("Превышено максимальное количество попыток.")
    return None  # Или любое значение по умолчанию, если нужно


def get_sort_option(prompt, options):
    """Эта функция просит пользователя выбрать вариант сортировки и проверяет,
    что выбранный вариант соответствует одному из допустимых (в данном случае
    1 или 2)."""
    while True:
        try:
            choice = int(input(prompt))
            if choice not in options:
                print(f"Ошибка: введите одно из доступных значений: {options}.")
                continue
            return choice
        except ValueError:
            print("Ошибка: введите корректное целое число.")


def user_interface():
    """Функция для взаимодействия с пользователем."""
    hh_api = HeadHunterAPI()
    json_handler = JSONFileHandler()  # Создаем экземпляр вашего обработчика JSON

    # Ввод поискового запроса
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    if not hh_vacancies:
        print("Не удалось получить вакансии.")
        return

    # Преобразование вакансий в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Получение числа вакансий для вывода
    top_n = get_positive_integer("Введите количество вакансий для вывода в топ N: ")
    if top_n is None:  # Проверка на случай, если количество попыток превышено
        print("Не удалось получить корректное количество вакансий, завершаем программу.")
        return

    # Фильтрация по ключевым словам
    filter_word = input("Введите ключевое слово для фильтрации вакансий в описании или оставьте пустым для пропуска: ")
    filtered_vacancies = [
        v
        for v in vacancies_list
        if (v.description and filter_word.lower() in v.description.lower()) or not filter_word
    ]

    # Выбор критерия сортировки
    sort_prompt = "Выберите критерий сортировки (1 - по зарплате, 2 - по дате размещения): "
    sort_option = get_sort_option(sort_prompt, [1, 2])

    # Дальнейшая логика программы
    print(f"Вы выбрали {top_n} вакансий и сортировку по {'зарплате' if sort_option == 1 else 'дате размещения'}.")

    if sort_option == 1:
        sorted_vacancies = sorted(
            filtered_vacancies, key=lambda x: x.salary if isinstance(x.salary, (int, float)) else 0, reverse=True
        )[:top_n]
    else:
        sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x.url, reverse=True)[:top_n]

    # Печать найденных вакансий
    if sorted_vacancies:
        print(f"Найдено {len(sorted_vacancies)} вакансий:")
        for v in sorted_vacancies:
            print(f"\nВакансия: {v.title}\nURL: {v.url}\nЗарплата: {v.salary}\nОписание: {v.description}\n")

        # Запрашиваем пользователя, хочет ли он удалить предыдущие данные
        delete_previous = input("Хотите ли вы удалить предыдущие данные для записи новых? (да/нет): ").strip().lower()

        # Если пользователь хочет удалить предыдущие данные
        if delete_previous == "да":
            json_handler.clear()  # Очищаем файл
            print("Предыдущие данные удалены.")
            for vacancy in sorted_vacancies:  # Сохраняем новые вакансии
                json_handler.save(vacancy.to_dict())
            print(f"Новые данные сохранены в {json_handler._JSONFileHandler__filename}.")
        else:  # Если пользователь не хочет удалять, добавляем новые данные к существующим
            for vacancy in sorted_vacancies:
                json_handler.save(vacancy.to_dict())
            print(f"Новые данные добавлены в {json_handler._JSONFileHandler__filename}.")
    else:
        print("По вашему запросу ничего не найдено.")


if __name__ == "__main__":
    user_interface()
