import pytest
from decorators import my_sum


@pytest.mark.parametrize(('a', 'b', 'expected_result'), (
    (2, 6, 8),
    (10, 20, 30),
    (-2, 2, 0),
))
def test_my_sum_with(a, b, expected_result):
    result = my_sum(a, b)
    assert result == expected_result
