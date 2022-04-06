# Tree

## Introduction
A tree is like a linked list. The difference is that in trees there can be more than one node next, but only one before. We more commonly use binary trees. Which limit the nodes after to just two. One in the right and one in the left. Just like in the picture below. There is something called a binary search tree. This kind of tree organizes values greater to the parent node to the right of it and values that are less than the parent node to the left of the parent node. 

![This is an image](tree.png))



## Python implementation
In python a tree is implemented by using classes. The insertion is a recursive process that finds the right spot to put the node you are trying to add. 
## Common operations efficiency
| Common Queue Operation | Big O notation efficiency |
| ---------------------- | --------------------------|
| insert | O(log n)
| remove | O(log n)
| memeber | O(log n)s
| size | O(1)

## Example
As an example we will create a binary search tree in no specific order of importnat years in world history. 


```
class BST:
        
    class Node:

        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)
    def _insert(self, data, node):

        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

tree = BST()
tree.insert(1975)
tree.insert(1830)
tree.insert(2019)
tree.insert(1929) 
```

## Probelm
Problem: Create a binary search tree with a given list of numbers inserting them in the order they are presented in the list and count the nodes to the nearest leaf. 

### Possible Solution

```
class BST:

    class Node:

        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None
            

    def __init__(self):

        self.root = None
        self.count = 0
        self.distances_to_root = []

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):

        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

         
    def __iter__(self):

        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
       
        if node is not None:
            self.count += 1
            yield from self._traverse_forward(node.left)
            
            yield node.data
            
            yield from self._traverse_forward(node.right)
            
        else:
            self.reset_count()

    def reset_count(self):
        if self.count != 0:
            self.distances_to_root.append(self.count)
        self.count = 0
            
# list of numbers: [6,3,5,1,8]

tree = BST()
tree.insert(6)
tree.insert(3)
tree.insert(5)
tree.insert(1)
tree.insert(8)

for node in tree:
    pass

print(min(tree.distances_to_root))

```
[Go back to Home Page](0-welcome.md)
