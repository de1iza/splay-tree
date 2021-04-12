from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, key: T):
        self.left = None
        self.right = None
        self.key = key

    # returns size of subtree
    def size(self) -> int:
        left_size: int = 0 if self.left is None else self.left.size()
        right_size: int = 0 if self.right is None else self.right.size()
        return left_size + right_size + 1

    # returns height of subtree
    def height(self) -> int:
        left_height: int = -1 if self.left is None else self.left.height()
        right_height: int = -1 if self.right is None else self.right.height()
        return max(left_height, right_height) + 1


class SplayTree:
    def __init__(self, key: T = None):
        if key is None:
            self.root = None
        else:
            self.root = Node(key)

    # left rotate helper
    def __rotate_left(self, v: Node) -> Node:
        tmp_node: Node = v.right
        v.right = tmp_node.left
        tmp_node.left = v
        return tmp_node

    # right rotate helper
    def __rotate_right(self, v: Node) -> Node:
        tmp_node: Node = v.left
        v.left = tmp_node.right
        tmp_node.right = v
        return tmp_node

    # splay helper function
    def __splay_left(self, root: Node, key: T) -> Node:
        if root.left is None:
            return root
        if key < root.left.key:
            root.left.left = self.__splay(root.left.left, key)
            root = self.__rotate_right(root)
        elif key > root.left.key:
            root.left.right = self.__splay(root.left.right, key)
            if root.left.right is not None:
                root.left = self.__rotate_left(root.left)
        if root.left is None:
            return root
        return self.__rotate_right(root)

    # splay helper function
    def __splay_right(self, root: Node, key: T) -> Node:
        if root.right is None:
            return root
        if key < root.right.key:
            root.right.left = self.__splay(root.right.left, key)
            if root.right.left is not None:
                root.right = self.__rotate_right(root.right)
        elif key > root.right.key:
            root.right.right = self.__splay(root.right.right, key)
            root = self.__rotate_left(root)
        if root.right is None:
            return root
        return self.__rotate_left(root)

    # splay key in the tree where node is a root
    def __splay(self, node: Node, key: T) -> Node:
        if node is None:
            return None
        if key < node.key:
            return self.__splay_left(node, key)
        elif key > node.key:
            return self.__splay_right(node, key)
        return node

    # inserts key.
    # if it was in the tree does nothing
    def insert(self, key: T) -> None:
        if self.root is None:
            self.root = Node(key)
            return
        if self.root.key == key:
            return
        self.root = self.__splay(self.root, key)
        if key < self.root.key:
            tmp_node: Node = Node(key)
            tmp_node.left = self.root.left
            tmp_node.right = self.root
            self.root.left = None
            self.root = tmp_node
        else:
            tmp_node: Node = Node(key)
            tmp_node.right = self.root.right
            tmp_node.left = self.root
            self.root.right = None
            self.root = tmp_node

    # removes key from the tree.
    # if key wasn't in the tree does nothing
    def remove(self, key: T) -> None:
        if self.root is None:
            return
        self.root = self.__splay(self.root, key)
        if key != self.root.key:
            return
        if self.root.left is None:
            self.root = self.root.right
        else:
            tmp_node: Node = self.root.right
            self.root = self.root.left
            self.__splay(self.root, key)
            self.root.right = tmp_node

    # returns True is key is in the tree
    def find(self, key: T) -> bool:
        if self.root is None:
            return False
        self.root = self.__splay(self.root, key)
        return key == self.root.key

    # returns size of the tree
    def size(self) -> int:
        if self.root is None:
            return 0
        return self.root.size()

    # returns size of the tree (tree with 1 node has 0 height)
    def height(self) -> int:
        if self.root is None:
            return -1
        return self.root.height()



