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

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

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

    def add_to_head(self, value):
        new_head = ListNode(value)
        self.length += 1
        # if empty
        if not self.head and not self.tail:
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

    def remove_from_head(self):
        copy_head = copy.copy(self.head.value)
        if not self.head:
            return
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return copy_head
        else:
            self.head = self.head.next
            self.head.next.delete()
            self.length -= 1
            return copy_head

    def add_to_tail(self, value):
        new_tail = ListNode(value)
        self.length += 1
        # if empty
        if not self.head and not self.tail:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail

    def remove_from_tail(self):
        copy_tail = copy.copy(self.tail.value)
        if not self.tail:
            return
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            next_tail = self.tail.prev
            # new tail will have no next value
            next_tail.next = None
            # sever connection
            self.tail.prev = None
            self.tail = next_tail
            return copy_tail

    def move_to_front(self, node):
        # already at front
        if node is self.head:
            return
        # if list contains single node
        elif self.head is self.tail:
            return
        else:
            # make a reference to create new node in a second
            temp_val = node.value
            self.delete(node)
            self.add_to_head(temp_val)

    def move_to_end(self, node):
        # node already is tail
        if node is self.tail:
            return
        # one value in list
        elif self.head is self.tail:
            return
        # empty
        elif not self.head and not self.tail:
            return
        else:
            # make a reference to create new node instance right after
            temp_val = node.value
            self.delete(node)
            self.add_to_tail(temp_val)

    def delete(self, node):
        # if list has single node
        if self.head is self.tail and self.head is node:
            self.head = None
            self.tail = None
            self.length = 0
        # if empty
        elif not self.head and not self.tail:
            return
        else:
            # if node is the head
            if not node.prev and node is self.head:
                self.remove_from_head()
            # if node is tail
            elif not node.next and node is self.tail:
                self.remove_from_tail()
            else:
                node.delete()

    def get_max(self):
        curr_node = self.head
        max_value = self.head.value
        while curr_node.next is not None:
            if curr_node.next.value > max_value:
                max_value = curr_node.next.value

            curr_node = curr_node.next

        return max_value
