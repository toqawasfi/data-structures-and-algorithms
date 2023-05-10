import pytest 
from animal_shelter.animal_shelter import  AnimalShelter,Animal
def test_enqueue_Cat():
    shelter = AnimalShelter()
    
    actual = shelter.enqueue(Animal('Whiskers','Cat'))
    expected = ['Whiskers']
    assert actual == expected
def test_enqueue_Cats():
    shelter = AnimalShelter()
    shelter.enqueue(Animal('Fluffy','Cat'))
    shelter.enqueue(Animal('yuio','Cat'))
    
    actual = shelter.enqueue(Animal('Whiskers','Cat'))
    expected = ['Fluffy', 'yuio', 'Whiskers']
    assert actual == expected
def test_enqueue_dog():
    shelter = AnimalShelter()
  
    actual = shelter.enqueue(Animal('rex','Dog'))
    expected = ['rex'] 
    assert actual == expected
def test_enqueue_dogs():
    shelter = AnimalShelter()
    shelter.enqueue(Animal('Doggy','Dog'))
    shelter.enqueue(Animal('Boby','Dog'))
    
    actual = shelter.enqueue(Animal('Rex','Dog'))
    expected = ['Doggy', 'Boby', 'Rex']
    assert actual == expected
   
def test_one_dequeue():
    shelter = AnimalShelter()
    shelter.enqueue(Animal('Doggy','Dog'))
    shelter.enqueue(Animal('Boby','Dog'))
    
    actual = shelter.dequeue('Dog')
    expected = "Doggy"
    assert actual == expected

def test_multi_dequeue():
    shelter = AnimalShelter()
    shelter.enqueue(Animal('Doggy','Dog'))
    shelter.enqueue(Animal('Boby','Dog'))
    actual = shelter.dequeue('Dog')
    
    actual = shelter.dequeue('Dog')
    expected = "Boby"
    assert actual == expected

