class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        output = ""
        current = self.head
        while current:
            output += f"{current.value} -> "
            current = current.next
        output += "Null"
        return output

    def __repr__(self):
     if self.head is None:
        return "Empty LinkedList"
     current = self.head
     nodes = []
     while current:
        nodes.append(str(current.value))
        current = current.next
     return " -> ".join(nodes)

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, value):
        node = Node(value)
        current = self.head
        self.head = node
        node.next = current

    @staticmethod
    def zip_lists(l1, l2):
        '''
        zip_lists a Method responsible for merging two linked lists alternativly 
        args:
        2 linked lists
        returns:
        zipped linked list

        '''
        if not l1.head:
            return l2
        if not l2.head:
            return l1
        result = LinkedList()
        current = result.head = Node()
        while l1.head and l2.head:
            current.next = l1.head
            l1.head = l1.head.next
            current = current.next
            current.next = l2.head
            l2.head = l2.head.next
            current = current.next
        if l1.head:
            current.next = l1.head
        if l2.head:
            current.next = l2.head
        result.head = result.head.next
        return result
   
    
    