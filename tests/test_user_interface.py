import os
import sys
import unittest
from unittest.mock import patch

from src.user_interface import get_positive_integer, get_sort_option

# Добавляем путь к src в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestUserInputFunctions(unittest.TestCase):

    @patch("builtins.input", side_effect=["5"])
    def test_get_positive_integer_valid(self, mock_input):
        result = get_positive_integer("Введите положительное число: ")
        self.assertEqual(result, 5)

    @patch("builtins.input", side_effect=["-5", "5"])
    def test_get_positive_integer_negative(self, mock_input):
        result = get_positive_integer("Введите положительное число: ")
        self.assertEqual(result, 5)

    @patch("builtins.input", side_effect=["abc", "5"])
    def test_get_positive_integer_non_integer(self, mock_input):
        result = get_positive_integer("Введите положительное число: ")
        self.assertEqual(result, 5)

    @patch("builtins.input", side_effect=["1"])
    def test_get_sort_option_valid(self, mock_input):
        result = get_sort_option("Выберите сортировку: ", [1, 2])
        self.assertEqual(result, 1)

    @patch("builtins.input", side_effect=["3", "1"])
    def test_get_sort_option_invalid(self, mock_input):
        result = get_sort_option("Выберите сортировку: ", [1, 2])
        self.assertEqual(result, 1)

    @patch("builtins.input", side_effect=["abc", "1"])
    def test_get_sort_option_non_integer(self, mock_input):
        result = get_sort_option("Выберите сортировку: ", [1, 2])
        self.assertEqual(result, 1)

    @patch("builtins.input", side_effect=["2"])
    def test_get_sort_option_valid_input(self, mock_input):
        result = get_sort_option("Выберите сортировку: ", [1, 2])
        self.assertEqual(result, 2)  # Проверяем, что возвращается правильное значение

    @patch("builtins.input", side_effect=["3"])
    def test_get_sort_option_invalid_input(self, mock_input):
        with patch("builtins.input", side_effect=["3", "2"]):  # Для второго вызова
            result = get_sort_option("Выберите сортировку: ", [1, 2])
            self.assertEqual(result, 2)  # Проверяем, что возвращается правильное значение после другого ввода


if __name__ == "__main__":
    unittest.main()
