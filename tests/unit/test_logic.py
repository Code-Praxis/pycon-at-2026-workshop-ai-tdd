import pytest

from src.shopping_cart.main import format_hi


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Alice", "Hi, Alice"),
        ("Bob", "Hi, Bob"),
    ],
)
def test_format_hi_should_correctly_format_greeting(name: str, expected: str) -> None:
    """Unit test: Verify name interpolation in greeting string."""
    assert format_hi(name) == expected
