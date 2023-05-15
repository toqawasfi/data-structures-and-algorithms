import pytest
from stack_queue_brackets.brackets import validate_brackets

def test_pattren1(str="{}"):
    actual=validate_brackets(str)
    expected=True
    assert actual== expected

def test_pattren2(str="{}(){}"):
    actual=validate_brackets(str)
    expected=True
    assert actual== expected

def test_pattren3(str="()[[Extra Characters]]"):
    actual=validate_brackets(str)
    expected=True
    assert actual== expected

def test_pattren4(str="(){}[[]]"):
    actual=validate_brackets(str)
    expected=True
    assert actual== expected

def test_pattren5(str="{}{Code}[Fellows](())"):
    actual=validate_brackets(str)
    expected=True
    assert actual== expected

def test_pattren6(str="[({}]"):
    actual=validate_brackets(str)
    expected=False
    assert actual== expected

def test_pattren7(str="(]("):
    actual=validate_brackets(str)
    expected=False
    assert actual== expected

def test_pattren8(str="{(})"):
    actual=validate_brackets(str)
    expected=False
    assert actual== expected