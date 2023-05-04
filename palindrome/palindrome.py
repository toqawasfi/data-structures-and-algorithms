class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def is_palindrome(self):
        if self.head is None:
            return True

        # find the middle node of the linked list
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # compare the first half with the reversed second half
        left = self.head
        right = prev
        while right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.next

        return True
# create a linked list
ll = LinkedList()
ll.add_node('r')
ll.add_node('a')
ll.add_node('c')
ll.add_node('e')
ll.add_node('c')
ll.add_node('a')
ll.add_node('r')

# check if the linked list is a palindrome
if ll.is_palindrome():
    print("True")
else:
    print("False")
