# A Node is the building block of a linked list.
# Each node stores some data AND a reference (pointer) to the next node.
class Node:
    def __init__(self, data):
        self.data = data      # the value this node holds
        self.next = None      # pointer to the next node (None means "end of list")


# LinkedList manages the chain of nodes.
# It only keeps track of the HEAD — the first node in the chain.
class LinkedList:
    def __init__(self):
        self.head = None      # an empty list has no head yet

    # append() adds a new node at the END of the list
    def append(self, data):
        new_node = Node(data)

        # if the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # otherwise, walk all the way to the last node
        current = self.head
        while current.next is not None:   # keep going until .next is None
            current = current.next

        current.next = new_node           # attach the new node at the end

    # delete() removes the first node that contains the given value
    def delete(self, data):
        # if list is empty, nothing to delete
        if self.head is None:
            return

        # special case: the node to delete is the head itself
        if self.head.data == data:
            self.head = self.head.next    # just move head forward
            return

        # otherwise, find the node BEFORE the one we want to delete
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next   # skip over the target node
                return
            current = current.next

    # display() prints out every value in the list in order
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")   # marks the end of the list


# --- main program ---
ll = LinkedList()

ll.append(10)     # list: 10 -> NULL
ll.append(20)     # list: 10 -> 20 -> NULL
ll.append(30)     # list: 10 -> 20 -> 30 -> NULL
ll.append(40)     # list: 10 -> 20 -> 30 -> 40 -> NULL

print("After appending:")
ll.display()      # Output: 10 -> 20 -> 30 -> 40 -> NULL

ll.delete(20)     # remove the node holding 20

print("After deleting 20:")
ll.display()      # Output: 10 -> 30 -> 40 -> NULL
