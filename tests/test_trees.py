import pytest
from Trees.tree import Binary_Tree,Binary_Search_Tree

def test_empty_tree():
    tree = Binary_Search_Tree(None) 
  
    actual= tree.print_nodes()
    expected=['None']
    assert actual == expected

def test_one_node():
    tree = Binary_Search_Tree(5) 
  
    actual= tree.value
    expected=5
    assert actual == expected
def test_left_right_node():
    tree = Binary_Search_Tree(5) 
    tree.Add(3)
    tree.Add(15)
  
    actual= tree.print_nodes()
    expected=['3', '5', '15']
    assert actual == expected

def test_in_order():
    my_arr=[]
    tree = Binary_Search_Tree(5) 
    tree.Add(3)
    tree.Add(15)
    tree.in_order(my_arr)
  
    actual= my_arr
    expected=[3, 5, 15]
    assert actual == expected

def test_pre_order():
    my_arr=[]
    tree = Binary_Search_Tree(5) 
    tree.Add(3)
    tree.Add(15)
    tree.pre_order(my_arr)
  
    actual= my_arr
    expected=[5, 3, 15]
    assert actual == expected

def test_post_order():
    my_arr=[]
    tree = Binary_Search_Tree(5) 
    tree.Add(3)
    tree.Add(15)
    tree.post_order(my_arr)
  
    actual= my_arr
    expected=[3, 15, 5]
    assert actual == expected

def test_max_right():
    tree = Binary_Search_Tree(5) 
    tree.Add(3)
    tree.Add(15)
  
    actual= tree.tree_max()
    expected=15
    assert actual == expected
def test_max_root():
    tree = Binary_Search_Tree(30) 
    tree.Add(3)
    tree.Add(15)
  
    actual= tree.tree_max()
    expected=30
    assert actual == expected