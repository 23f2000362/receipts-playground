from calc import add, clamp


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


def test_clamp_low():
    assert clamp(-5, 0, 10) == 0


def test_clamp_middle():
    assert clamp(5, 0, 10) == 5
