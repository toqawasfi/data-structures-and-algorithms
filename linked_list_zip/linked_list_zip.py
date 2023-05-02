from  linked_list_zip. nodez import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty LinkedList"
        else:
            current = self.head
            while current:
                output += f'{{{current.value}}} -> '
                current = current.next
            output += "NULL"
        return output

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def zipLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    dummy = Node()
    curr = dummy
    while head1 is not None and head2 is not None:
        curr.next = head1
        head1 = head1.next
        curr = curr.next
        curr.next = head2
        head2 = head2.next
        curr = curr.next
    if head1 is not None:
        curr.next = head1
    elif head2 is not None:
        curr.next = head2
    return dummy.next


