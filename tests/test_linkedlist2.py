import pytest
from linkedlist2.linkedlist2 import LinkedList2
from linkedlist2.node2 import Node

def test_empty_LL():
    LL = LinkedList2()

    actual = str(LL)
    expected = "Empty LinkeList"
    assert actual == expected

def test_append_to_end():
    
    LL= LinkedList2()

    LL.append(1)
    LL.append(2)
    LL.append(3)

    actual = str(LL)
    expected = "{1 }-> {2 }-> {3 }->  Null"
  
    assert actual == expected

def test_insert_before_middle():
    LL= LinkedList2()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)

    LL.insert_before(3, 6)

    actual = str(LL)
    expected = "{1 }-> {2 }-> {6 }-> {3 }-> {4 }->  Null"
  
    assert actual == expected

def test_insert_before_first_node():
    LL= LinkedList2()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)

    LL.insert_before(LL.head.value, 6)

    actual = str(LL)
    expected = "{6 }-> {1 }-> {2 }-> {3 }-> {4 }->  Null"
  
    assert actual == expected

def test_insert_after_middle():
    LL= LinkedList2()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)

    LL.insert_after(2, 6)

    actual = str(LL)
    expected = "{1 }-> {2 }-> {6 }-> {3 }-> {4 }->  Null"
  
    assert actual == expected


def test_insert_after_last_node():
    LL= LinkedList2()

    LL.append(1)
    LL.append(2)
    LL.append(3)
    LL.append(4)

    LL.insert_after(4, 6)

    actual = str(LL)
    expected = "{1 }-> {2 }-> {3 }-> {4 }-> {6 }->  Null"
  
    assert actual == expected