class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data    # set data as given
        self.next = None    # initialize pointer as None

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """
    MAX_SIZE = 5

    def __init__(self, value):
        """Initialize the stack with an empty state."""
        new_node = Node(value)  # temporary new node with given data
        self.rear = new_node
        self.top = new_node
        self.top.next = self.rear   # link node to self (circular)
        self.size = 1               # initial size is 1

    def push(self, value):
        """Add a new Temperature object to the stack, replacing the oldest entry if full."""
        new_node = Node(value)      # temporary new node with given data
        if self.size == 0:          # edge case: stack is empty (similar implementation to constructor)
            self.rear = new_node
            self.top = new_node
            self.top.next = self.rear
            self.size = 1
        elif self.size == self.MAX_SIZE:    # edge case: stack is full
            new_node.next = self.rear.next  # newest data node points to second-oldest
            self.rear = new_node.next       # second-oldest data node is now the new rear
            self.top.next = new_node        # previous newest data now points to newly added newest
            self.top = new_node             # newest data is now the new top
        else:                           # base case: stack not full
            new_node.next = self.rear   # newest data node points to oldest
            self.top.next = new_node    # previous newest data now points to newly added newest
            self.top = new_node         # newest data is now the new top
            self.size += 1              # increment stack size

    def pop(self):
        """Remove the oldest entry from the stack."""
        if self.size == 0:  # edge case: list is empty
            return None
        else:                               # base case: list not empty
            temp = self.rear                # temporary variable to store oldest data
            if self.size == 1:              # edge case: list has only one element
                self.rear = None                # set rear to None
                self.top = None                 # set top to None
                self.size = 0                   # size = 0 (list is empty)
                return temp                     # return temporary stored data
            self.top.next = self.rear.next  # newest node now points to second oldest (oldest is being removed)
            self.rear = self.top.next       # second oldest becomes new oldest
            self.size -= 1                  # decrement list size
            return temp                     # return removed data (oldest)

    def peek(self):
        """Return the most recent temperature entry without removing it."""
        return self.top

    def print_stack(self):
        """Print all stored readings in order from oldest to newest."""
        print()                     # print empty line (formatting)
        temp = self.rear            # temporary node starts at oldest
        for i in range(self.size):  # iterate through oldest to newest
            print(temp.data)        # print each node
            temp = temp.next        # traverse to next newest

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return self.size == 0
