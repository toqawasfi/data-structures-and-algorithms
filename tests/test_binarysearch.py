import pytest
from BinarySearch.binarysearch import binarysearch

def case1_test():
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