class Node():
   def __init__(self, value):
      self.value = value
      self.next = None

   def __repr__(self):
        return str(self.value)

class my_stack():
   """
   A class that implements a stack data structure.
   """

   def __init__(self):
      """
      Initializes an empty stack.
      """
      self.top = None
      self.size = 0

   def __str__(self):
      """
      Returns a string representation of the stack.
      """
      output = ""
      current = self.top
      while current:
         output += f"{current.value} -> "
         current = current.next
      return output

   def __repr__(self):
      """
      Returns a string representation of the stack.
      """
      if self.top is None:
         return "Empty Stack"
      current = self.top
      nodes = []
      while current:
         nodes.append(str(current.value))
         current = current.next
      return " -> ".join(nodes)

   def is_empty(self):
      """
      Returns True if the stack is empty, False otherwise.
      """
      return self.size == 0

   def push(self, value):
      """
      Adds a new node with the given value to the top of the stack.
      """
      node = Node(value)
      if self.top:
         node.next = self.top
      self.top = node
      self.size += 1

   def pop(self):
      """
      Removes and returns the node at the top of the stack.
      Raises an exception if the stack is empty.
      """
      if self.top is not None:
         temp = self.top.value
         self.top = self.top.next
         self.size -= 1
         return temp
      else:
         raise Exception("Stack is empty")

   def peek(self):
      """
      Returns the value of the node at the top of the stack.
      Raises an exception if the stack is empty.
      """
      if self.top is None:
         raise Exception("Stack is empty")
      return self.top.value

class pseudo_queue():
   """
   A class that implements a queue data structure using two stacks.
   """

   def __init__(self):
      """
      Initializes an empty queue.
      """
      self.size = 0
      self.my_stack1 = my_stack()
      self.my_stack2 = my_stack()

   def enqueue(self, value):
      """
      Adds a new node with the given value to the end of the queue.
      """
      while not self.my_stack1.is_empty():
         self.my_stack2.push(self.my_stack1.pop())

      self.size += 1
      self.my_stack2.push(value)
      return self.my_stack2

   def dequeue(self):
      """
      Removes and returns the node at the front of the queue.
      Raises an exception if the queue is empty.
      """
      while not self.my_stack2.is_empty():
         self.my_stack1.push(self.my_stack2.pop())

      self.size -= 1
      return self.my_stack1.pop()

   def __str__(self):
      """
      Returns a string representation of the queue.
      """
   def __str__(self):
        output = ""
        current = self.my_stack1.top
        while current:
            output += f"{current.value} -> "
            current = current.next
        current = self.my_stack2.top
        while current:
            output += f"{current.value} -> "
            current = current.next
        return output

   def __repr__(self):
      """
      Returns a string representation of the queue.
      """
      if self.my_stack1.top is None:
         return "Empty Queue"
      current = self.my_stack1.top
      nodes = []
      while current:
         nodes.append(str(current.value))
         current = current.next

# test the implementation
# my_queue = pseudo_queue()
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# my_queue.enqueue(3)
# print(my_queue) # should print "1 -> 2 -> 3 -> "
# my_queue.dequeue() # should print "1"
# # print(my_queue.dequeue()) # should print "2"
# print(my_queue) # should print "3 -> "
