from typing import Any


def filter_by_currency_json(list_of_transactions: list[Any], currency: str):
    """Данная функция фильтрует список json по заданной валюте
    (в списке остаются только те транзакции у которых нужная валюта)"""
    my_list = []
    for i in list_of_transactions:
        if i.get("operationAmount").get("currency").get("code") == currency:
            my_list.append(i)
    return my_list


def filter_by_currency_csvxlsx(list_of_transactions: list[Any], currency: str):
    """Функция, фильтрующая список csv и xlsx по заданной валюте
    (то есть в списке остаются только те транзакции у которых нужная валюта)"""
    my_list = []
    for i in list_of_transactions:
        if i.get("currency_code") == currency:
            my_list.append(i)
    return my_list


def transaction_descriptions(list_of_transactions: list[Any]):
    """Функция, возвращающая описание транзакции"""
    for i in list_of_transactions:
        if i.get("description") is not None:
            yield i.get("description")


def card_number_generator(start: int, stop: int):
    """Эта функция генерирует номера карт в заданном диапазоне - от start до stop"""
    if start < 0 or stop > 9999999999999999:
        raise ValueError("Введены неправильные значения")
    else:
        index = start
        number = "0" * (16 - len(str(index))) + str(index)
        for i in range(start, stop + 1):
            yield f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
            index += 1
            number = "0" * (16 - len(str(index))) + str(index)
