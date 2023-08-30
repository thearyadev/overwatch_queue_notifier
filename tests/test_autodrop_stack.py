import sys
import pytest

sys.path.append(".")

from utils.autodrop_stack import AutoDropStack


def test_initialize():
    s = AutoDropStack(5)
    assert len(s.stack) == 0


def test_push_integer():
    s = AutoDropStack(5)
    s.push(1)
    assert len(s.stack) == 1
    assert s.stack[0] == 1


def test_push_string():
    s = AutoDropStack(5)
    s.push("Hello World")
    assert len(s.stack) == 1
    assert s.stack[0] == "Hello World"


def test_overflow():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    assert len(s.stack) == 5
    assert s.stack[0] == 2
    assert s.stack[1] == 3
    assert s.stack[2] == 4
    assert s.stack[3] == 5
    assert s.stack[4] == 6


def test_percentiles():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    assert s.percentiles() == {2: 0.2, 3: 0.2, 4: 0.2, 5: 0.2, 6: 0.2}


def test_percentiles_unfilled():
    s = AutoDropStack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.percentiles() == {
        1: 0.3333333333333333,
        2: 0.3333333333333333,
        3: 0.3333333333333333,
    }


def test_private_stack():
    s = AutoDropStack(5)
    with pytest.raises(AttributeError):
        s.__stack


def test_percentiles_empty_stack():
    s = AutoDropStack(5)
    assert s.percentiles() == {}
