import pytest
from linked_list_kth.node2 import Node
from linked_list_kth.linked_list_kth import LinkedList1


def test_k_bigger_than_the_length(link):
    with pytest.raises(Exception):
       link.kth_from_end(6)

def test_k_equal_to_the_length(link):
    with pytest.raises(Exception):
       link.kth_from_end(4)

def test_k_negative_number(link):
    with pytest.raises(Exception):
       link.kth_from_end(-1)

def test_k_the_first_and_the_only_index():
    link3 =  LinkedList1()
    link3.append(3)
    actual = link3.kth_from_end(0)
    expected = 3
    assert expected == actual

def test_k_in_the_middle(link):
    actual = link.kth_from_end(2)
    expected = "Happy Path"
    assert expected == actual

@pytest.fixture
def link():
    link = LinkedList1()
    link.append(1)
    link.append(3)
    link.append(8)
    link.append(2)
    return link