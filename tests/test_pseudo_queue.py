import pytest
from stack_queue_pseudo.stack_queue_pseudo import pseudo_queue
def test_enqueue_value():
    
    my_queue = pseudo_queue()
    
    actual = str(my_queue.enqueue(6))
    expected ="6 -> "
    assert actual == expected


def test_enqueue_multi_value():
    my_queue = pseudo_queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(3)
    actual = str(my_queue)
    expected = "3 -> 3 -> 2 -> 1 -> "
    assert actual == expected

def test_dequeue():
    s1 = pseudo_queue()
    
    s1.enqueue(1)
    s1.enqueue(2)
    s1.enqueue(3)
    s1.dequeue()
    
    actual = str(s1)
    expected = "2 -> 3 -> "
    assert actual == expected

def test_multipop_emptystack():
    q1 = pseudo_queue()
    
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    actual = str(q1)
    expected = ""
    assert actual == expected
