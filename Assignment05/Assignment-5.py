# Defining TreeNode class
class TreeNode : 
    def __init__(self, name, phone_number ):
    # Initializing the node with a name and phone number
        self.name = name
        self.phone_number = phone_number
    # Refering to the left and right children 
        self.left = None
        self.right = None

# Defining the BinarySearchTree class
class BinarySearchTree:
    def __init__(self):
    # Initializing the tree with an empty root
        self.root = None 

    def insert(self, name, phone_number):   # Implementing insert method
        # Creating a new node with the given name and phone number
        new_node = TreeNode(name, phone_number)
        # If the tree is empty, setting the new node as the root node
        if self.root is None:
            self.root = new_node
        else:
            # If not, inserting the node in the correct position
            self._insert_node(self.root, new_node)

        
    def _insert_node(self, current_node, new_node):  # Recursively finding the correct position for the new node
        if new_node.name < current_node.name:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_node(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_node(current_node.right, new_node)
    
    def search(self, name): # Implementing search method
        # search for a node by name and return phone number
        return self._find_node(self.root, name)
    
    def _find_node(self, current_node,name):
        # recursively search for the node with the given name
        if current_node is None:
            return None
        if name == current_node.name:
            return current_node.phone_number
        elif name < current_node.name:
            return self._find_node(current_node.left, name)
        else:
            return self._find_node(current_node.right, name)
    
    def inorder_traversal(self):
        # Perform an in order traversal and return the result
        result = []
        self._inorder_node(self.root, result)
        return result
    
    def _inorder_node(self, current_node, result):
        # Recursively traverse the tree in order
        if current_node is not None:
            self._inorder_node(current_node.left, result)
            result.append((current_node.name, current_node.phone_number))
            self._inorder_node(current_node.right, result)

    def delete(self, name):
        # Delete a node by name 
        self.root = self._remove_node(self.root, name)

    def _remove_node(self, current_node, name):
        # Recursively find and remove the node with the given name
        if current_node is None:
            return current_node
        if name < current_node.name:
            current_node.left = self._remove_node(current_node.left, name)
        elif name > current_node.name:
            current_node.right = self._remove_node(current_node.right, name)
        else:
            # Node with only one child or no child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            # Node with two children: get the in order successor
            temp = self._find_min(current_node.right)
            current_node.name = temp.name
            current_node.phone_number = temp.phone_number
            current_node.right = self._remove_node(current_node.right, temp.name)
        return current_node

    def _find_min(self, node):
        # Find the node with the minimum value (left most node)
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    
bst = BinarySearchTree()
bst.insert("Shivam", "123-679-2799")
bst.insert("Yash", "234-679-3434")
bst.insert("Zakir", "786-786-7866")

print(bst.search("Shivam"))  # Output: 123-456-7890
print(bst.search("Rohan"))    # Output: None

print(bst.inorder_traversal())  # Output: [('Shivam', '123-679-2799'), ('Yash', '234-679-3434'), ('Zakir', '786-786-7866')]

bst.delete("Yash")
print(bst.inorder_traversal())  # Output: [('Shivam', '123-679-2799'), ('Zakir', '345-678-9012')]

bst.insert("Abhishek", "456-789-0123")
bst.delete("Shivam")
print(bst.inorder_traversal())  # Expected Output: [('Abhishek', '456-789-0123'), ('Zakir', '786-786-7866')]

bst.insert("Raghav", "567-890-1234")
bst.delete("Yash")
print(bst.inorder_traversal())  # Expected Output: [('Abhishek', '456-789-0123'), ('Raghav', '567-890-1234'), ('Zakir', '786-786-7866')]


