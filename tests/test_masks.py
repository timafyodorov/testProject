import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def masks_card() -> str:
    return "5385882263548596"


def test_masks_card(masks_card: str) -> None:
    assert get_mask_card_number(masks_card) == "5385 88 ** 8596"


def test_masks_account() -> None:
    assert get_mask_account("96354521441242052365") == "**2365"