"""Some simple tests."""
import pytest
import random
from datetime import datetime
random.seed(datetime.now())


func = lambda x: x + 1

def test_answer_0():
    assert random.choice([True, False]) == True

def test_answer_1():
    assert random.choice([True, False]) == True

def test_answer_2():
    assert random.choice([True, False]) == True
