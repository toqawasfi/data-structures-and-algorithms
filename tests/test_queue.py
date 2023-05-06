import pytest 
from  stack_queue.queue import My_queue

def test_enqueue_value():
    
    q1 = My_queue()
    q1.enqueue(5)
    actual = q1.front.value
    expected =5
    assert actual == expected

def test_enqueue_multi_values():
    q1 = My_queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    
    actual = str(q1)
    expected = "1 -> 2 -> 3 -> "
    assert actual == expected

def test_dequeue():
    s1 = My_queue()
    
    s1.enqueue(1)
    s1.enqueue(2)
    s1.enqueue(3)
    s1.dequeue()
    
    actual = str(s1)
    expected = "2 -> 3 -> "
    assert actual == expected

def test_multipop_emptystack():
    q1 =  My_queue()
    
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    actual = str(q1)
    expected = ""
    assert actual == expected

def test_peek():
    s1 = My_queue()
    s1.enqueue(1)
    s1.enqueue(2)
    s1.enqueue(3)
    
    actual = str(s1.peek())
    expected = "1"
    assert actual == expected

def test_empty_stack():
    q = My_queue()
    assert q.front is None
    assert q.size == 0

def test_dequeue_peek_on_empty_stack():
    q= My_queue()
    try:
        q.dequeue()
        assert False, "Expected Exception not raised"
    except Exception as e:
        assert str(e) == "its empty", f"Unexpected Exception raised: {e}"
        
    try:
        q.peek()
        assert False, "Expected Exception not raised"
    except Exception as e:
        assert str(e) == "its empty", f"Unexpected Exception raised: {e}"