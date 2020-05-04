<h1 align="center">Pybush 🌲</h1>

[![PyPI version](https://badge.fury.io/py/pybush.svg)](https://badge.fury.io/py/pybush)
[![version](https://img.shields.io/badge/dynamic/json?color=orange&label=version&prefix=v&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fnikhil0360%2Fpybush%2Fmaster%2Fsetup.json)](https://pypi.org/project/pybush/1.0.0/)
[![python vesrion](https://img.shields.io/badge/dynamic/json?color=blue&label=Python&query=pythonv&url=https%3A%2F%2Fraw.githubusercontent.com%2Fnikhil0360%2Fpybush%2Fmaster%2Fsetup.json)](https://www.python.org/downloads/)
[![](https://img.shields.io/badge/dynamic/json?color=ff69b4&label=Dependency&prefix=pip%20install%20&query=dependency&url=https%3A%2F%2Fraw.githubusercontent.com%2Fnikhil0360%2Fpybush%2Fmaster%2Fsetup.json)](https://pypi.org/project/binarytree/)


a python module (created by me 😉) to implement bst, bbst, avl trees and more in Python3+

### Overview:
[binarytree](https://pypi.org/project/binarytree/) is a great module to implement trees in python. Since python doesn't support pointers;
implementing binary tree functions was a bit tricky, but no more 😁. **pybush** brings this functionality using binarytree module. Now you can do everything from creating a tree, printing the tree, implement avl, do rotations and other functions.

binarytree has a pretty print functionality, which prints the tree in a visual way that we normally see while learning.
```
example: a level order bst [7,3,11,1,5,9,13,0,2,4,6,8,10,12,14] will look like this


            ______7_______
           /              \
        __3__           ___11___
       /     \         /        \
      1       5       9         _13
     / \     / \     / \       /   \
    0   2   4   6   8   10    12    14
```
binarytree do have a lot of functionalities, but pybush extends it...

## Getting started
```
$ pip3 install binarytree
$ pip3 install pybush
```

pybush have the following Class to implement a Node:
```
class Node(Node):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.h = self.height
        self.count = 1
```
## Funtions for BBST (Balance binary search tree)
* create a bbst
```
>>> values = [1,2,3,4,5,6,7,8]
>>> tree_root = create_bbst(values,0,len(values)-1)
>>> print(tree_root)

    __4__
   /     \
  2       6
 / \     / \
1   3   5   7
             \
              8
```
* add a Node
```
>>> add(tree_root,6.5)
Node(6.5)
>>> print(tree_root)

    __4__
   /     \
  2       6
 / \     / \
1   3   5   7
           / \
        6.5   8
```
* delete a Node
```
>>> delete(tree_root,7)
>>> print(tree_root)

    __4__
   /     \
  2       6_
 / \     /  \
1   3   5   6.5
               \
                8
```

* search for a Node
```
>>> search(tree_root,3)
Node(3)
```

* Predecessor and Successor
```
>>> successor(tree_root,4)
Node(5)
>>> predecessor(tree_root,6)
Node(5)
```

* least common ancestor
```
>>> lca(tree_root,5,8)
Node(6)
>>> print(tree_root)

    __4__
   /     \
  2       6_
 / \     /  \
1   3   5   6.5
               \
                8
```

* rangecount and rangelist
```
>>> rangecount(tree_root,1,5)
5
>>> list = []
>>> rangelist(tree_root,1,5,list)
>>> list
[Node(5), Node(4), Node(3), Node(2), Node(1)]
```
## Functions for AVL tree
* create a avl tree
```
>>> values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
>>> tree_root = create_bbst(values,0,len(values)-1)
```
* add a Node
```

>>> print(tree_root)

        ______8________
       /               \
    __4__           ____12___
   /     \         /         \
  2       6       10         _14
 / \     / \     /  \       /   \
1   3   5   7   9    11    13    15

>>> add_avl(tree_root,7.2)
>>> print(tree_root)

        ______8________
       /               \
    __4__           ____12___
   /     \         /         \
  2       6       10         _14
 / \     / \     /  \       /   \
1   3   5   7   9    11    13    15
             \
             7.2

>>> add_avl(tree_root,7.4)
>>> print(tree_root)

        ______________8________
       /                       \
    __4__                   ____12___
   /     \                 /         \
  2       6___            10         _14
 / \     /    \          /  \       /   \
1   3   5     7.2_      9    11    13    15
             /    \
            7     7.4

# see the subtree rotated
```
* delete a Node
```
>>> delete_avl(tree_root,12)
>>> print(tree_root)

>>> print(tree_root)

        ______________8_____
       /                    \
    __4__                   _11___
   /     \                 /      \
  2       6___            10      _14
 / \     /    \          /       /   \
1   3   5     7.2_      9       13    15
             /    \
            7     7.4
```
* search a Node
```
>>> search(tree_root,9)
Node(9)
```
* check whether a tree is a avl tree
```
>>> is_avl(tree_root)
True
```
* find rank and rank of a Node
```
>>> print(tree_root)

        ______________8_____
       /                    \
    __4__                   _11___
   /     \                 /      \
  2       6___            10      _14
 / \     /    \          /       /   \
1   3   5     7.2_      9       13    15
             /    \
            7     7.4

>>> rank(tree_root,10)
5
>>> find_rank(tree_root,5)
Node(10)
```
