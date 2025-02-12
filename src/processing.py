from datetime import datetime
from typing import Any


def filter_by_state(list_of_operations: Any, state: str = "EXECUTED") -> Any:
    """
    Эта функция фильтрует список словарей на основе состояния. В строке объясняются аргументы
    и то, что возвращает функция
    """
    new_list = []
    for i in list_of_operations:
        if i["state"] == state:
            new_list.append(i)
    return new_list


def sort_by_date(list_of_dict: Any, reverse: bool = False) -> Any:
    """
    Эта функция сортирует список словарей по полю в порядке убывания или возрастания. В строке объясняются аргументы
    и то, что возвращает функция (отсортированный список)
    """
    return sorted(
        list_of_dict, key=lambda date: datetime.strptime(date["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse
    )


dic = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(dic))
print(sort_by_date(dic))
