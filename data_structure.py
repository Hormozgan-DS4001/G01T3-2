from typing import List, Optional


class HeapPriority:
    class Node:
        def __init__(self, data, key):
            self.data = data
            self.key = key

    def __init__(self, size: int = 200):
        self.array: List[Optional[HeapPriority.Node]] = [None] * size
        self.last = 0

    def __iter__(self):
        count = 0
        while count < self.last:
            yield self.array[count].data
            count += 1

    def __getitem__(self, item):
        return self.array[item]

    def _insert(self, data, key):
        assert self.last < len(self.array)
        new_node = self.Node(data, key)
        self.array[self.last] = new_node
        if self.last == 0:
            self.last += 1
            return

        child = self.last
        par = (self.last - 1) // 2

        while par >= 0 and self.array[child].key > self.array[par].key:
            self.array[child], self.array[par] = self.array[par], self.array[child]
            child = par
            par = (child - 1) // 2

        self.last += 1

    def _pop(self):
        assert self.last > 0

        self.last -= 1
        res = self.array[0]
        self.array[0] = self.array[self.last]

        par = 0
        left = 1
        right = 2

        while True:
            max_heap = par
            if self.array[left] and self.array[left].key > self.array[max_heap].key:
                max_heap = left
            if self.array[right] and self.array[right].key > self.array[max_heap].key:
                max_heap = right
            if max_heap == par:
                break
            self.array[par], self.array[max_heap] = self.array[max_heap], self.array[par]
            par = max_heap
            left = (par * 2) - 1
            right = (par * 2) - 2

        return res

    def pop_insert(self, data, key):
        assert self.last < len(self.array), "is full"
        new_node = self.Node(data, key)

        res = self.array[0]
        self.array[0] = new_node

        par = 0
        left = 1
        right = 2

        while True:
            max_heap = par
            if self.array[left] and self.array[left].key > self.array[max_heap].key:
                max_heap = left
            if self.array[right] and self.array[right].key > self.array[max_heap].key:
                max_heap = right
            if max_heap == par:
                break
            par = max_heap
            left = (par * 2) + 1
            right = (par * 2) + 2

        return res

    def update(self, index, key):
        self.array[index].key = key
        child = index
        par = (child - 1) // 2
        while par >= 0 and self.array[child].key > self.array[par].key:
            self.array[child], self.array[par] = self.array[par], self.array[child]
            child = par
            par = (child - 1) // 2

    def find(self):
        return self.array[0]

    def enqueue(self, data, key):
        self._insert(data, key)

    def dequeue(self):
        return self._pop()


class DLL:
    class _Node:
        def __init__(self, data, key):
            self.data = data
            self.key = key
            self.next = None
            self.prev = None

    class NodeHandler:
        def __init__(self, node, dll):
            self.node = node
            self.dll = dll

        def next(self):
            self.node = self.node.next

        def prev(self):
            self.node = self.node.prev

        def get(self):
            return self.node.value

        def delete(self):
            if not self.node.next:
                self.dll.remove(len(self.dll))

            if not self.node.prev:
                self.dll.remove(0)

            else:
                self.node.prev.next = self.node.next
                self.node.next.prev = self.node.prev
                self.dll._length -= 1

        def traverse(self, reverse=False):
            while self.node:
                yield self.node.data
                if not reverse:
                    if not self.node.next:
                        break
                    self.node = self.node.next
                else:
                    if not self.node.prev:
                        break
                    self.node = self.node.prev

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __getitem__(self, key):
        assert isinstance(key, int), 'Index must be an integer'
        assert 0 <= key < self._length, 'Index out of range'

        temp = self._head
        counter = 0

        while temp:
            if counter == key:
                return temp.value
            temp = temp.next
            counter += 1

    def __setitem__(self, key, value):
        assert isinstance(key, int), 'Index must be an integer'
        assert 0 <= key < self._length, 'Index out of range'

        temp = self._head
        counter = 0

        while temp:
            if counter == key:
                temp.value = value
            temp = temp.next
            counter += 1

    def __iter__(self):
        temp = self._head
        while temp:
            yield temp.data, temp.key
            temp = temp.next

    def __str__(self):
        if self._length == 0:
            return 'DLL[]'

        res = 'DLL['
        temp = self._head

        while temp:
            res += f'{str(temp.value)}, '
            temp = temp.next

        return f'{res[:-2]}]'

    __repr__ = __str__

    def __len__(self):
        return self._length

    def __get(self, index):
        if index <= self._length // 2:
            temp = self._head
            counter = 0
            while counter < index:
                temp = temp.next
                counter += 1
        else:
            temp = self._tail
            counter = self._length
            while counter > index:
                temp = temp.prev
                counter -= 1
        return temp

    def get_node_handler(self, index):
        return self.NodeHandler(self.__get(index), self)

    def insert(self, index, data, key):
        assert isinstance(index, int), 'Index must be an integer'
        assert 0 <= index <= self._length, 'Index out of range'

        new_node = self._Node(data, key)

        if self._length == 0:
            self._head = new_node
            self._tail = new_node

        elif index == 0:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        elif index == self._length:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        else:
            prev_node = self.__get(index - 1)
            prev_node.next.prev = new_node
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node

        self._length += 1

    def remove(self, index):
        assert isinstance(index, int), 'Index must be an integer'
        assert self._length != 0, 'Linked list is empty'
        assert 0 <= index <= self._length, 'Index out of range'

        if self._length == 1:
            self._head = None
            self._tail = None

        elif index == 0:
            next_node = self._head.next
            next_node.prev = None
            self._head = next_node

        elif index == self._length - 1:
            prev_node = self._tail.prev
            prev_node.next = None
            self._tail = prev_node

        else:
            current_node = self.__get(index)
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev

        self._length -= 1

    def prepend(self, data, key):
        self.insert(0, data, key)

    def append(self, data, key):
        self.insert(self._length, data, key)

    def pop(self):
        res = self._tail
        self.remove(self._length - 1)
        return res.data, res.key

    def enqueue(self, data, key):
        new_node = self._Node(data, key)
        if self._head is None:
            self._head = new_node
            self._tail = new_node

        else:
            t = self._tail
            while t.key < key:
                if not t.prev:
                    self._head.prev = new_node
                    new_node.next = self._head
                    self._head = new_node
                t = t.prev

            if t is self._tail:
                t.next = new_node
                new_node.prev = t
                self._tail = new_node

            else:
                new_node.next = t.next
                t.next = new_node
                new_node.prev = t
                t.next.prev = new_node
        self._length += 1

    def dequeue(self):
        res = self._head

        if self._head is self._tail:
            self._head = None
            self._tail = None

        else:
            self._head = self._head.next
            self._head.prev = None
        self._length -= 1

        return res.data, res.key

    @property
    def tail(self):
        return self._tail

    @property
    def head(self):
        return self._head
