import pytest
from sortinsert.sortinsert import insertsort
def test_Reverse_sorted():
    actual=insertsort([20,18,12,8,5,-2],3)
    expected= [-2, 3, 5, 8, 12, 18, 20]
    assert actual== expected

def test_Reverse_sorted():
    actual=insertsort([5,12,7,5,5,7],3)
    expected= [3, 5, 5, 5, 7, 7, 12]
    assert actual== expected

def test_Reverse_sorted():
    actual=insertsort([2,3,5,7,13,11],3)
    expected=[2, 3, 3, 5, 7, 11, 13]
    assert actual== expected


