import pytest
from linked_list_zip.nodez import Node
from linked_list_zip.linked_list_zip import LinkedList
def test_empty_l1():
    l1 = LinkedList()
    l2 = LinkedList()
    l2.insert(6)
    l2.insert(5)
    l2.insert(4)
    expected ='4 -> 5 -> 6 -> Null'
    actual = LinkedList.zip_lists(l1, l2)
    assert expected == str(actual)

def test_empty_l2():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.insert(6)
    l1.insert(5)
    l1.insert(4)
    expected ='4 -> 5 -> 6 -> Null'
    actual = LinkedList.zip_lists(l1, l2)
    assert expected == str(actual)

def test_same_length_lists():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.insert(6)
    l1.insert(5)
    l1.insert(4)
    l2.insert(3)
    l2.insert(2)
    l2.insert(1)
    expected ='4 -> 1 -> 5 -> 2 -> 6 -> 3 -> Null'
    actual = LinkedList.zip_lists(l1, l2)
    assert expected == str(actual)

def test_different_length_lists():
    l1 = LinkedList()
    l2 = LinkedList()
    l1.insert(6)
    l1.insert(5)
    l2.insert(3)
    l2.insert(2)
    l2.insert(1)
    expected ='5 -> 1 -> 6 -> 2 -> 3 -> Null'
    actual = LinkedList.zip_lists(l1, l2)
    assert expected == str(actual)

# def test_empty_l2():
#     l1 =Node(2,  Node(4,  Node(6)))
#     l2 = None
#     expected = l1 
#     actual = LinkedList.zip_lists(l1, l2)
#     assert expected == actual

# def test_l1_l2():
#     l1 = Node(1,  Node(3,  Node(5)))
#     l2 =  Node(2,  Node(4))
#     expected  =  Node(1,  Node(2,  Node(3,  Node(4,  Node(5)))))
#     actual= LinkedList.zip_lists(l1, l2) 
#     assert expected == actual
# def test_different_length_lists():
#     l1 = Node(1, Node(3, Node(5)))
#     l2 = Node(2, Node(4, Node(6)))
#     expected = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
#     actual = LinkedList.zip_lists(l1, l2)
#     assert expected == actual
#     assert id(expected) == id(actual)




