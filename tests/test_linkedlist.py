# import pytest
# from linkedlist.linkedlist import LinkedList
# from linkedlist.node1 import Node

# def test_empty_LL():
#     ll = LinkedList()

#     actual = repr(ll)
#     expected = "Empty LinkedList"
#     assert actual == expected


# # Test insert node
# def test_insert_node(ll):
    
#     expected = "Toqa -> Null"
#     actual = str(ll)
#     assert expected == actual

# def test_insert_multiple_nodes():
#     ll = LinkedList()

#     ll.insert('a')
#     ll.insert('b')
#     ll.insert('c')

#     actual = str(ll)
#     expected = "c -> b -> a -> Null"
#     assert actual == expected

# def test_value_in_LL():
#     ll = LinkedList()
#     ll.insert(9)
#     ll.insert(10)
#     ll.insert(11)

#     actual = ll.includes(10)
#     expected = True
#     assert actual == expected

# def test_value_in_LL():
#     ll = LinkedList()
#     ll.insert(9)
#     ll.insert(10)
#     ll.insert(11)

#     actual = ll.includes(10)
#     expected = True
#     assert actual == expected

    

# def test_value_not_in_LL():
#     ll = LinkedList()
#     ll.insert(9)
#     ll.insert(10)
#     ll.insert(11)

#     actual = ll.includes(5)
#     expected = False
#     assert actual == expected



# def test_values():
#     ll = LinkedList()
#     ll.insert(9)
#     ll.insert(10)
#     ll.insert(11)

#     actual = str(ll)
#     expected = "11 -> 10 -> 9 -> Null"
#     assert actual == expected
    

# @pytest.fixture
# def ll():
#     ll = LinkedList()
#     ll.insert("Toqa")
#     return ll
