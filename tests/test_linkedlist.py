import pytest
from linkedlist.linkedlist import LinkedList
from linkedlist.node import Node
def test_empty_ll():
    ll = LinkedList()
    expected = "Empty LinkeList"
    actual = str(ll)
    assert expected == actual


# Test insert node
def test_insert_node(ll):
    
    expected = "{Toqa }->  Null"
    actual = str(ll)
    assert expected == actual

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert("Toqa")
    return ll
