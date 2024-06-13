import pytest

from main.operations import sum, sub, multi

@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (50, 50, 100),
        (0, 0, 0),
        (687, 13, 700),
    ]
)


def test_sum(a, b, result):
    assert sum(a, b) == result


@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (10, 10, 100),
        (33, 0, 0),
        (6, 6, 36),
    ]
)


def test_multi(a, b, result):
    assert multi(a, b) == result


@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (4, 2, 2),
        (100, 50, 50),
        (1, 0, 1),
    ]
)


def test_sub(a, b, result):
    assert sub(a, b) == result