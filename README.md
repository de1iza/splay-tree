# splay-tree
A splay tree is a binary search tree with the additional property that recently accessed elements are quick to access again.
## Supported operations
* **insert(key)** &mdash; inserts key in the tree (does nothing if key exists);
* **remove(key)** &mdash; removes key from the tree (does nothing if key doesn't exist);
* **find(key)** &mdash; returns True is key exists and False if doesn't;
* **size()** &mdash; returns size of the tree (number of nodes);
* **height()**  &mdash; returns height of the tree (size of a tree with 1 node is 0).
## Example
```
tree = SplayTree()
tree.insert(2)
tree.find(1)
tree.remove(2)
```
## Running tests
 `py.test -v tests/test_tree.py`
 
