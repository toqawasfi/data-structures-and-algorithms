import pytest
from Hash_table.hash import Hashtable

def test_set():
    ht = Hashtable()
    ht.set("apple", 5)
    assert ht.get("apple") == 5

def test_get_existing_key():
    ht = Hashtable()
    ht.set("apple", 5)
    assert ht.get("apple") == 5

def test_get_non_existing_key():
    ht = Hashtable()
    assert ht.get("banana") == None

def test_keys():
    ht = Hashtable()
    ht.set("apple", 5)
    ht.set("banana", 7)
    ht.set("orange", 3)
    assert set(ht.keys()) == {"apple", "banana", "orange"}

def test_collision_handling():
    ht = Hashtable(size=2)
    ht.set("apple", 5)
    ht.set("papel", 7)  # Collision with "apple"
    assert ht.get("apple") == 5
    assert ht.get("papel") == 7

def test_retrieve_value_from_collision_bucket():
    ht = Hashtable(size=2)
    ht.set("apple", 5)
    ht.set("papel", 7)  # Collision with "apple"
    assert ht.get("apple") == 5
    assert ht.get("papel") == 7

def test_hash_in_range():
    ht = Hashtable(size=100)
    key = "apple"
    hash_value = ht.hash(key)
    assert 0 <= hash_value < 100
