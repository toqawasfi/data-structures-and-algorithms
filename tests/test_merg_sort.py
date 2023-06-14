import pytest
import 

def test_Reverse_sorted():
    actual=insertsort([20,18,12,8,5,-2],3)
    expected= [-2, 3, 5, 8, 12, 18, 20]
    assert actual== expected