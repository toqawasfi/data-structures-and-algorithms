import pytest 
from  stack_queue.stack import (my_stack)

def test_push_value():
    
    s1 = my_stack()
    s1.push(5)
    actual = s1.top.value
    expected =5
    assert actual == expected

def test_push_multi_values():
    s1 = my_stack()
    
    s1.push(1)
    s1.push(2)
    s1.push(3)
    
    actual = str(s1)
    expected = "3 -> 2 -> 1 -> "
    assert actual == expected

def test_pop():
    s1 = my_stack()
    
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.pop()
    
    actual = str(s1)
    expected = "2 -> 1 -> "
    assert actual == expected

def test_multipop_emptystack():
    s1 = my_stack()
    
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.pop()
    s1.pop()
    s1.pop()
    actual = str(s1)
    expected = ""
    assert actual == expected

def test_peek():
    s1 = my_stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    
    actual = str(s1.peek())
    expected = "3"
    assert actual == expected

def test_empty_stack():
    s = my_stack()
    assert s.top is None
    assert s.size == 0

# def test_pop_peek_on_empty_stack():
#     s = my_stack()
#     try:
#         s.pop()
#         assert False, "Expected Exception not raised"
#     except Exception as e:
#         assert str(e) == "its empty", f"Unexpected Exception raised: {e}"
        
#     try:
#         s.peek()
#         assert False, "Expected Exception not raised"
#     except Exception as e:
#         assert str(e) == "its empty", f"Unexpected Exception raised: {e}"