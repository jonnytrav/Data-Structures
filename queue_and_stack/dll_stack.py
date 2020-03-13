# from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')

import copy


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        curr_node = self.head

        output = ''

        while curr_node.next is not None:
            output += f'{curr_node.value}'
            curr_node = curr_node.next

        return output

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        # if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # if list contains one item
        elif self.head == self.tail:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        self.length -= 1
        copy_head = copy.copy(self.head.value)
        # contains single value
        if self.head == self.tail:
            self.delete(self.head)
            return copy_head
        # if empty
        elif self.head == None and self.tail == None:
            return
        else:
            self.delete(self.head)
            return copy_head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        # list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # if length is one
        elif self.head is self.tail:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        copy_tail = copy.copy(self.tail.value)
        self.length -= 1
        # contains single value
        if self.head == self.tail:
            # completely sever both references
            self.tail.next = None
            self.tail.prev = None
            self.head.next = None
            self.head.prev = None
            self.tail = None
            self.head = None
            return copy_tail
        elif self.head == None and self.tail == None:
            return "Nothing to be removed!"
        else:
            # hold reference to prev value
            next_tail = self.tail.prev
            # new tail will have no next value
            next_tail.next = None
            # sever connection
            self.tail.prev = None
            self.tail = next_tail
            return copy_tail

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        # if length of list is one
        elif self.head is self.tail:
            return
        else:
            # make a reference to create new node instance
            temp_val = node.value
            self.delete(node)
            self.add_to_head(temp_val)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # if node to be moved to end is already on the end
        if node is self.tail:
            return
        # if length of list is one
        elif self.head is self.tail:
            return

        else:
            # make a reference to create new node instance
            temp_val = node.value
            self.delete(node)
            self.add_to_tail(temp_val)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):

        # if linked list has one value, meaning head == tail
        if self.head is self.tail and self.head is node:
            self.head = None
            self.tail = None
            self.length = 0
            return
        # if linked list is empty
        elif self.length is 0 and self.head is None and self.tail is None:
            return
        else:
            # if deleted node is the head
            if node.prev is None:
                self.head = node.next
                node.delete()
            # if deleted node is the tail
            elif node.next is None:
                self.tail = node.prev
                node.delete()
            else:
                node.delete()

            self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        # starting point
        curr_node = self.head
        max_value = self.head.value
        while curr_node.next is not None:
            if curr_node.next.value > max_value:
                max_value = curr_node.next.value

            curr_node = curr_node.next

        return max_value


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?

        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size is 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size
