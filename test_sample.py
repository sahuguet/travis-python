"""Some simple tests."""
import pytest

func = lambda x: x + 1

def test_answer_0():
    assert func(3) == 5

def test_answer_1():
    assert func(3) == 4

def test_answer_2():
    assert func(3) == 5
