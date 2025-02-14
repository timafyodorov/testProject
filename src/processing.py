def filter_by_state(values: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Эта функция фильтрует список словарей на основе состояния. В строке объясняются аргументы
    и то, что возвращает функция
    """
    new_list = []
    for value in values:
        if value.get("state") == state:
            new_list.append(value)
    return new_list


def sort_by_date(list_of_dict: list[dict], setting: bool = True) -> list[dict]:
    """
    Эта функция сортирует список словарей по полю в порядке убывания или возрастания. В строке объясняются аргументы
    и то, что возвращает функция (отсортированный список)
    """
    sorted_list = sorted(list_of_dict, key=lambda date: date["date"], reverse=setting)
    return sorted_list
