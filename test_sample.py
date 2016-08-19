"""Some simple tests."""
import pytest

import random
from datetime import datetime
random.seed(datetime.now())

import sys

import subprocess
import hashlib

def md5(str):
	m = hashlib.md5()
	m.update(str)
	return m.hexdigest()

func = lambda x: x + 1

def test_answer_0():
    assert random.choice([True, False]) == True

def test_answer_1():
    assert random.choice([True, False]) == True

def test_answer_2():
    assert random.choice([True, False]) == True

def test_answer_3():
    assert random.choice([True, False]) == True

def test_answer_4():
    assert random.choice([True, False]) == True

def test_answer_5():
    assert random.choice([True, False]) == True

def test_answer_6():
    assert random.choice([True, False]) == True

def test_answer_7():
    assert random.choice([True, False]) == True

def test_answer_8():
    assert random.choice([True, False]) == True

def test_answer_9():
    assert random.choice([True, False]) == True

def test_answer_10():
    assert random.choice([True, False]) == True

def test_script_01():
	with open('script_01', 'r') as myfile:
		cmd = myfile.read().strip()
	output = subprocess.check_output(cmd, shell=True)
	assert md5(output) == '91a929dbba4ba1daf218e0525b180eed'

"""
This is the kind of encoding we should be able to do for each homework.
"""

@pytest.mark.parametrize("script,fun,expected", [
    ("script_01", lambda x: md5(x), "91a929dbba4ba1daf218e0525b180eed"),
    ("script_02", lambda x: int(x), 1001),
    ("script_03", lambda x: int(x), 470),
    ("script_04", lambda x: int(x), 531),
    ("script_05", lambda x: md5(x), "a8021368eb5d7140f7510b68fbf34feb"),
    ("script_06", lambda x: md5(x), "a983fdb78b76d61424bda3ae55a0119f"),
])
def test_script(script, fun, expected):
	with open(script, 'r') as myfile:
		cmd = myfile.read().strip()
	output = subprocess.check_output(cmd, shell=True)
	assert fun(output) == expected
