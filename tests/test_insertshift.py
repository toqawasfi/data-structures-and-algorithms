import pytest
from arrayinsertshift.insertShiftArray import insertShiftArray

def test_odd_leng():
     actual = insertShiftArray([1,2,3,4,5],6)
     expected = [1, 2, 3, 6, 4, 5]
     assert actual == expected

def test_even_leng():
     actual = insertShiftArray([1,2,3,4],5)
     expected = [1, 2, 5, 3, 4]
     assert actual == expected

