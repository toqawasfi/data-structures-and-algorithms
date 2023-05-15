class Animal:
    '''
    A class to add name & species  properities
    '''
    def __init__(self, name, species):
        self.name = name
        self.species = species
    

    
    def __str__(self):
        return self.name
    

class  AnimalShelter():
    def __init__(self):
        '''
        A class to creat animal instances as a queue including enqueue & dequeue methods

        '''
            
        
        self.cat_queue=[]
        self.dog_queue=[]
        self.container=[]
        self.container1=[]

    def enqueue(self,animal):
      '''
      Method to push animals to queues based on species
      args:animal(str)
      return:None
      
      '''
      if animal.species == "Cat":
            self.cat_queue.append(animal.name)
           
            return self.cat_queue

        
      elif animal.species == "Dog":
            self.dog_queue.append(animal.name)
            return self.dog_queue

        
    def dequeue(self, pref):
         '''
      Method to remove animals from queues based on user input
      args:pref(str)
      return:object
      
      '''
         if pref=="Cat":
            if len(self.cat_queue)==0 and not self.container:
                return "I Have no cats"
        
            while len(self.cat_queue)!=0:
                self.container.append(self.cat_queue.pop())
        
            return self.container.pop()
    
         elif pref=="Dog":
            #  if len(self.dog_queue)==0:
            #     return "I Have no Dogs"
            
             while len(self.dog_queue)!=0:
                self.container1.append(self.dog_queue.pop())
            #  self.cat_queue= self.container1
            
             return self.container1.pop()
         
 


        
          
    

shelter = AnimalShelter()

cat1 = Animal("Whiskers", "Cat")
print(shelter.enqueue(cat1))
print(shelter.enqueue(Animal('Fluffy','Cat')))
print(shelter.enqueue(Animal('yuio','Cat')))
print(shelter.dequeue('Cat'))
print(shelter.dequeue('Cat'))
print(shelter.dequeue('Cat'))

# # # print(shelter.dequeue('Dog'))
print(shelter.enqueue(Animal('Rex', 'Dog')))
print(shelter.enqueue(Animal('Rex2', 'Dog')))

