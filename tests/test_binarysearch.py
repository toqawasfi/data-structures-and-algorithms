import pytest
from BinarySearch.binarysearch import binarysearch

def test_case1():
    actual=binarysearch([1,2,3,4,5,6,7],2)
    expected=1
    assert actual == expected

def test_case2():
    actual=binarysearch([1,2,6,7],6)
    expected=2
    assert actual == expected

def test_case3():
    actual=binarysearch([1,2,3,4,5,6],3)
    expected=2
    assert actual == expected

def test_case4():
    actual=binarysearch([2,3,4,5,6],1)
    expected=-1
    assert actual == expected

def test_case5():
    actual=binarysearch([11, 22, 33, 44, 55, 66, 77], 90)
    expected=-1
    assert actual == expected

def test_case6():
    actual=binarysearch([-131, -82, 0, 27, 42, 68, 179], 42)
    expected=4
    assert actual == expected