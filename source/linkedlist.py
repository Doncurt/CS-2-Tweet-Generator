#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        #points to current node as the head
        current_node = self.head
        #current number of nodes seen so far
        total = 0

        #interation. exits once at the last node
        while current_node.next != None:
            #increments total
            total+=1
            #goes to the next node and starts the process again
            current_node = current_node.next
        return total

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        #first create a new node
        new_node = node(data)
        #stores the node that were currently working on, starts at the left most point
        current_node = self.head
        #starts atthe left most point, then interates over all of the node, and once the next node of the current node is none, we know that that is the last and then can insert
        while current_node.next!= None:
            current_node = current_node.next
        #once we know we're at the last element of the list, we set the next node to the new node
        current_node.next = new_node
        #length to figure out how many nodes are in the list itslef
    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        #make sure you cant go past the last node
        if index >= self.length():
            print("GET index out of range")
            return None
        #contains the current index that were looking at
        current_index = 0
        #the current node that were looking at, starts off at head
        current_node = self.head
        while True:
            #increments the current node( at the beginning it will be the head node)
            current_node= current_node.next
            #if the current index is equal to the one passed in
            if current_index == index:
                #return the data of that node
                 return current_node.data
             #otherwise, increment the current index and keep going
            current_index +=1

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if index >= self.length():
            print("GET index out of range")
            return None
        #looks at the current index
        current_index = 0
        current_node = self.head
        while True:
            #when a node is being erased, after the node is erased, you have to make sure the node previous to it points to the node after the one you erased
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                #when node is being erased, just the pointers are changed
                last_node.next = current_node.next
                #breaks out and returns, changing the list an setting it
                return
            #if its not found you increase the indexing
            current_index+=1


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
