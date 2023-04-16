import pytest
from BinarySearch.binarysearch import binarysearch

def test_case1():
    actual=binarysearch([1,2,3,4,5,6,7],2)
    expected=1
    assert actual == expected

def case2_test():
    actual=binarysearch([1,2,6,7],6)
    expected=2
    assert actual == expected

def case3_test():
    actual=binarysearch([1,2,3,4,5,6],3)
    expected=2
    assert actual == expected

def case4_test():
    actual=binarysearch([2,3,4,5,6],1)
    expected=-1
    assert actual == expected

def case5_test():
    actual=binarysearch([11, 22, 33, 44, 55, 66, 77], 90)
    expected=-1
    assert actual == expected

def case6_test():
    actual=binarysearch([-131, -82, 0, 27, 42, 68, 179], 42)
    expected=4
    assert actual == expected