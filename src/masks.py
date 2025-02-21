def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты по правилу XXXX XX** **** XXXX."""
    if len(card_number) < 16:
        return "Некорректный номер карты"
    card_number_str = str(card_number)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета по правилу **XXXX."""
    if len(account_number) < 20:
        return "Некорректный номер счета"
    account_number_str = str(account_number)
    return "**" + account_number_str[-4:]
print(get_mask_account("234"))