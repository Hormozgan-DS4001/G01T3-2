from typing import List, Optional


class HeapPriority:
    class Node:
        def __init__(self, data, key):
            self.data = data
            self.key = key

    def __init__(self, size: int = 200):
        self.array: List[Optional[HeapPriority.Node]] = [None] * size
        self.last = 0

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

    def enqueue(self, data, key):
        self._insert(data, key)

    def dequeue(self):
        return self._pop()









