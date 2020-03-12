"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
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
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
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
            self.head.next = None
            self.head.prev = None
            self.tail.next = None
            self.tail.prev = None
            self.head = None
            self.tail = None
            return copy_head
        elif self.head == None and self.tail == None:
            return "Nothing to be removed!"
        else:
            # hold reference to next value
            next_head = self.head.next
            # new head will have no prev value
            next_head.prev = None
            # sever connection
            self.head.next = None
            self.head = next_head
            return copy_head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = None
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
        # NTS - ADD IF BLOCKS IN CASE GIVEN NODE == TAIL
        new_head = node
        # removes from current spot meaning adjust pointers
        new_head.next = self.head
        new_head.prev = None

        # now adjust the old head's pointers before removing head attribute
        self.head.prev = new_head

        self.head = new_head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    # def move_to_end(self, node):
    #     new_tail = node

    #     # tail cannot have a next
    #     new_tail.prev = self.tail
    #     new_tail.next = None

    #     # now adjust current tail's next pointer
    #     self.tail.next = new_tail

    #     # reassign the list's tail attribute
    #     self.tail = new_tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        to_be_deleted = node

        # if linked list has one value, meaning head == tail
        if self.head == self.tail and self.head == to_be_deleted:
            self.head = None
            self.tail = None
            self.length = 0
        # if linked list is empty
        elif self.length == 0 and self.head == None and self.tail == None:
            return "Nothing to be deleted!"
        else:
            # if deleted node is the head
            if to_be_deleted.prev == None:
                to_be_deleted.next.prev = None
                self.head = to_be_deleted.next
                to_be_deleted.next = None
            # if deleted node is the tail
            elif to_be_deleted.next == None:
                to_be_deleted.prev.next = None
                self.tail = to_be_deleted.prev
                to_be_deleted.prev = None

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
