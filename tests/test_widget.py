import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def get_dates() -> str:
    return "2019-07-03T18:35:29.512364"


@pytest.mark.parametrize(
    "data, result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79 ** 6361"),
    ],
)

def test_mask_account_card(data: str, result: str) -> None:
    assert mask_account_card(data) == result

def test_get_date(date_input: str) -> None:
    assert get_date(date_input) == "03.07.2019"

def test_get_date_2(date_input: str) -> None:
    assert get_date(date_input) == "05.11.2015"