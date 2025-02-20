import pytest

from src.masks import get_mask_account, get_mask_card_number

# Тестирование функции mask_card_number
def test_mask_card_number() -> None:
    """
    Тестирование функции mask_card_number. Проверяется, что номер карты правильно маскируется.
    """
    # Проверка корректного номера карты
    assert get_mask_card_number("1234567891234567") == "1234 56** **** 4567"
    # Проверка некорректного номера карты
    assert get_mask_card_number("12345") == "Некорректный номер карты"

# Тестирование функции mask_account_number
def test_mask_account_number() -> None:
    """
    Тестирование функции mask_account_number. Проверяется, что номер счета правильно маскируется.
    """
    # Проверка корректного номера счета
    assert get_mask_account("76666108430178874305") == "**4305"
    # Проверка некорректного номера счета
    assert get_mask_account("234") == "Некорректный номер счета"
