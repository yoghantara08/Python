from locale import currency
from turtle import position


class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class Linked_List:
    """
    Singly Linked List
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds new Node containing data at head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found
        Takes O(n) time
        """
        current = self.head

        while current != None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at
        the insertion point takes O(n) time.

        Takes overall O(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev = current
            next_node = current.next_node

            prev.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            
            while position < index:
                current = current.next_node
                position += 1
            return current

    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current != None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)

# l = Linked_List()
# N1 = Node(10)
# l.head = N1

# print(l.size())

# l = Linked_List()
# l.add(12)
# l.add(2)
# l.add(10)
# l.add(6)
# l.add(3)

# # n = l.search(6)
# insert = l.insert(5,2)

# remove = l.remove(3)

# print(l.size())
# print(l)
# print(n)
