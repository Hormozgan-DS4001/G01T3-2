class AVL:
    class _Node:
        def __init__(self, key):
            self.key = key
            self.right = None
            self.left = None
            self.height = 0

    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return self._Node(key)
        if key > root.key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)

        if self.get_height(root.left) > self.get_height(root.right):
            root.height = self.get_height(root.left) + 1
        else:
            root.height = self.get_height(root.right) + 1

        balance = self.get_balance(root)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    @staticmethod
    def get_height(root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, data):
        get_1 = data.left
        get_2 = get_1.right
        get_1.right = data
        data.left = get_2

        if self.get_height(data.left) > self.get_height(data.right):
            data.height = 1 + self.get_height(data.left)

        else:
            data.height = 1 + self.get_height(data.right)

        if self.get_height(get_1.left) > self.get_height(get_1.right):
            get_1.height = 1 + self.get_height(data.left)

        else:
            get_1.height = 1 + self.get_height(data.right)

        return get_1

    def left_rotate(self, data):
        get1 = data.right
        get2 = get1.left
        get1.left = data
        data.right = get2
        if self.get_height(data.left) > self.get_height(data.right):
            data.height = 1 + self.get_height(data.left)

        else:
            data.height = 1 + self.get_height(data.right)

        if self.get_height(get1.left) > self.get_height(get1.right):
            get1.height = 1 + self.get_height(data.left)

        else:
            get1.height = 1 + self.get_height(data.right)

        return get1

    def find(self, key):
        t = self.root
        while t:
            if t.key == key:
                return t, t.key
            if key > t.key:
                t = t.right
            else:
                t = t.left

    def show(self, root):
        if not root:
            return
        yield root.key
        yield from self.show(root.left)
        yield from self.show(root.right)

