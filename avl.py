class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance_factor = self.balance(root)

        # Rotaciones
        if balance_factor > 1 and key < root.left.key:  
            return self.rotate_right(root)

        if balance_factor < -1 and key > root.right.key:  
            return self.rotate_left(root)

        if balance_factor > 1 and key > root.left.key:  
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance_factor < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, key):
        if not root:
            return False
        if key == root.key:
            return True
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)
