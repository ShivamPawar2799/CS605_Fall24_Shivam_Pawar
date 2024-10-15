## Classes

### TreeNode
Represents a node in the binary search tree.

 **Attributes:**
  - `name`: The key (name) stored in the node.
  - `phone_number`: The value (phone number) stored in the node.
  - `left`: Reference to the left child node.
  - `right`: Reference to the right child node.

### BinarySearchTree
Represents the binary search tree and provides methods to manipulate the tree.

 **Methods:**
  - `__init__()`: Initializes an empty binary search tree.
  - `insert(name, phone_number)`: Inserts a new node with the given name and phone number.
  - `search(name)`: Searches for a node by name and returns the associated phone number.
  - `inorder_traversal()`: Returns a list of all nodes in the tree in sorted order.
  - `delete(name)`: Deletes a node by name from the tree.

## Usage

### Inserting Nodes
To insert a new node into the tree, use the `insert` method:

**Python**
bst = BinarySearchTree()
bst.insert("Shivam", "123-679-2799")
bst.insert("Yash", "234-679-3434")
bst.insert("Zakir", "786-786-7866")


### Searching for a Node
To search for a node by name and get the associated phone number, use the `search` method:

**Python**
phone_number = bst.search("Shivam")
print(phone_number)  # Output: 123-679-2799

phone_number = bst.search("Rohan")
print(phone_number)  # Output: None


### In-order Traversal
To get a list of all nodes in the tree in sorted order, use the `inorder_traversal` method:

**Python**
nodes = bst.inorder_traversal()
print(nodes)  # Output: [('Shivam', '123-679-2799'), ('Yash', '234-679-3434'), ('Zakir', '786-786-7866')]


### Deleting a Node
To delete a node by name from the tree, use the 'delete' method:

**Python**
bst.delete("Yash")
nodes = bst.inorder_traversal()
print(nodes)  # Output: [('Shivam', ('123-679-2799'), ('Zakir', '786-786-7866')]


## Edge Cases
The `delete` method handles the following edge cases:
- Deleting a node with no children.
- Deleting a node with one child.
- Deleting a node with two children (replaces the node with its in-order successor).

## Conclusion
This binary search tree implementation provides basic functionality for inserting, searching, and deleting nodes, as well as traversing the tree in order. It is a useful data structure for managing sorted data efficiently.




