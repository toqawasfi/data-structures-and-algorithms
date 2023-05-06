class Node():
   
   def __init__(self,value):
      self.value=value
      self.next=None
      
   

   def __repr__(self):
        return str(self.value)


class My_queue():
   def __init__(self):
      '''
      Initilizer constructor
      '''
      self.front= None
      self.rear=None
      self.size=0

   def __str__(self):
    '''
    Method to reformat the output from the user side
    '''
    output = ""
    current = self.front
    while current:
        output += f"{current.value} -> "
        current = current.next
    
    return output
   
   def __repr__(self):
    '''
    Method to reformat the output from the terminal side
    '''
    if self.top is None:
        return "Empty LinkedList"
    current = self.front
    nodes = []
    while current:
        nodes.append(str(current.value))
        current = current.next
    return " -> ".join(nodes)
 
   
   def is_empty(self,size):
      '''
      A method to check if my queue is empty
      args:
      int :size
      returns:
      Boolean 
      '''
      if size ==0:
         return True
      else:
         return False
         
      

   def enqueue(self,value):
    '''
    A method to add nodes to the front of my queue
    args: 
    int ,value
    return:
    None
    '''
    front=self.front
    rear=self.rear
    
    node=Node(value)
    # Case1:if Empty queue  
    if front ==None :
     self.front=node
     self.rear=node
     self.size+=1
     
    #case2:one node
    elif front ==rear:
     front.next =node
     self.rear =node
     self.size+=1

   #case3:Multiple Nodes
    else:
     
     self.rear.next=node
     self.rear=node
     self.size+=1

   def dequeue(self):
       '''
      A method to delete the front node from my queue
      args:None
      return:the value of deleted front node
      
       '''
       #case1:Empty Queue
       if self.front is None:
         if self.is_empty(self.size):
          raise Exception("its empty")
        
       #Case2: one node

       elif self.front == self.rear :
        
          temp=self.front.value
          self.front = None
          self.rear= None
         
          self.size-=1
          return temp
       #case3: Multiple nodes
       else:
         
          temp=self.front.value
          self.front= self.front.next
         
          self.size-=1
          return (temp)

   def peek(self):
    '''
   A method responsible for returning my front value
   args:None
   return: The value of my Front
     '''
    if self.front is None:
        if self.is_empty(self.size):
          raise Exception("its empty")
     
    return self.front.value
  
My_queue1=My_queue()
My_queue1.enqueue(8)
My_queue1.enqueue(4)
My_queue1.enqueue(5)
# # print( My_queue1.front)
# print( My_queue1.size)
My_queue1.dequeue()
print(My_queue1)




