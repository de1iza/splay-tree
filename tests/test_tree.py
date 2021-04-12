import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.splay_tree import SplayTree


def test_empty():
    tree = SplayTree()
    assert tree.size() == 0
    assert tree.height() == -1


def test_empty_remove():
    tree = SplayTree()
    tree.remove(5)
    tree.remove(2)


def test_empty_find():
    tree = SplayTree()
    assert tree.find(1) is False
    tree.insert(4)
    tree.insert(99)
    assert tree.find(99) is True
    tree.remove(99)
    tree.remove(4)
    assert tree.find(4) is False
    assert tree.find(99) is False


def test_insert():
    tree = SplayTree(88)
    tree.insert(12)
    tree.insert(100)
    tree.insert(1)
    tree.insert(-1)
    assert tree.find(12) is True
    assert tree.find(88) is True
    assert tree.find(10) is False


def test_remove():
    tree = SplayTree(2)
    tree.insert(1)
    tree.insert(0)
    tree.insert(50)
    tree.remove(2)
    tree.insert(-1)
    tree.insert(-7)
    tree.remove(0)
    assert tree.find(0) is False
    assert tree.find(2) is False
    assert tree.find(-1) is True
    assert tree.find(-7) is True


def test_find():
    tree = SplayTree(33)
    tree.insert(2)
    tree.insert(99)
    assert tree.find(200) is False
    tree.insert(200)
    assert tree.find(200) is True
    assert tree.find(33) is True
    assert tree.find(3) is False


def test_height():
    tree = SplayTree()
    tree.insert(1)
    tree.insert(5)
    tree.insert(22)
    assert tree.height() == 2
    tree.insert(4)
    tree.insert(90)
    assert tree.height() == 4
    tree.insert(100)
    tree.insert(3)
    assert tree.height() == 3
    tree.insert(12)
    assert tree.height() == 3
    tree.insert(2)
    assert tree.height() == 5
    tree.remove(22)
    tree.remove(3)
    assert tree.height() == 2
    tree.remove(10)
    assert tree.height() == 2


def test_size():
    tree = SplayTree()
    tree.insert(6)
    tree.insert(8)
    tree.insert(10)
    assert tree.size() == 3
    tree.insert(50)
    tree.insert(11)
    assert tree.size() == 5
    tree.remove(8)
    tree.remove(7)
    assert tree.size() == 4
    tree.remove(11)
    assert tree.size() == 3
