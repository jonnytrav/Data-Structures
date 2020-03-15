from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    # cache needs to have limit and curr_size attributes along with a DLL

    def __init__(self, limit=10):
        self.limit = limit
        self.curr_size = 0
        self.list = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # first check dict for key
        if key in self.storage:
            # utilize DLL methods
            self.list.move_to_front(self.storage[key])
            # this pair is now most recently used
            return self.storage[key].value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room.

    Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.

    """

    def set(self, key, value):
        # if in the dictionary already, update the pair
        if key in self.storage:
            ref_to_pair = self.storage[key]
            # update the pair
            ref_to_pair.value = (key, value)
            # make most recently used
            self.list.move_to_front(ref_to_pair)
            # instructions expect the value to be returned
            return ref_to_pair.value

        # if at max size alread
        if self.curr_size >= self.limit:
            # remove pair from dictionary FIRST
            del self.storage[self.list.tail.value[0]]
            # remove last item in DLL
            self.list.remove_from_tail()
            self.curr_size -= 1

        self.curr_size += 1
        self.list.add_to_head((key, value))
        self.storage[key] = self.list.head


lruc = LRUCache(3)
lruc.set("item1", 1)
print(lruc.get("item1"))
