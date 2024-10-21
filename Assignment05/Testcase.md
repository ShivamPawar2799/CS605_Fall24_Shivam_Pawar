# Test Document for Binary Search Tree

## Introduction
This document describes the test cases for the binary search tree (BST) implementation. Each test case includes the steps to perform, the expected outcome, and the actual observations.

## Test Cases

| Test Case | Description | Steps | Expected Outcome | Actual Observations |
|-----------|-------------|-------|------------------|---------------------|
| **1** | Inserting Nodes | 1. Create an instance of `BinarySearchTree`.<br>2. Insert the following nodes:<br>    - ("Shivam", "123-679-2799")<br>    - ("Yash", "234-679-3434")<br>    - ("Zakir", "786-786-7866") | The nodes should be inserted in the correct positions according to the BST properties. | Nodes were inserted correctly: "Shivam" as root, "Yash" as right child of "Shivam", and "Zakir" as right child of "Yash". |
| **2** | Searching for a Node | 1. Search for the node with the name "Shivam".<br>2. Search for a non-existent node with the name "Rohan". | - Searching for "Shivam" should return "123-679-2799".<br>- Searching for "Rohan" should return `None`. | - Searching for "Shivam" returned "123-679-2799".<br>- Searching for "Rohan" returned `None`. |
| **3** | In-order Traversal | 1. Perform an in-order traversal of the BST. | The traversal should return the nodes in sorted order: [("Shivam", "123-679-2799"), ("Yash", "234-679-3434"), ("Zakir", "786-786-7866")]. | In-order traversal returned: [("Shivam", "123-679-2799"), ("Yash", "234-679-3434"), ("Zakir", "786-786-7866")]. |
| **4** | Deleting a Node with No Children | 1. Delete the node with the name "Yash". | The node "Yash" should be removed from the BST. | Node "Yash" was removed successfully. |
| **5** | Deleting a Node with One Child | 1. Insert the node ("Abhishek", "456-789-0123") as the left child of "Shivam".<br>2. Delete the node with the name "Shivam". | The node "Shivam" should be removed, and "Abhishek" should take its place. | Node "Shivam" was removed, and "Abhishek" took its place. |
| **6** | Deleting a Node with Two Children | 1. Insert the node ("Raghav", "567-890-1234") as the left child of "Yash".<br>2. Delete the node with the name "Yash". | The node "Yash" should be removed, and the in-order successor should take its place. | Node "Yash" was removed, and the in-order successor took its place. |

## Conclusion
This document outlines the test cases for the binary search tree implementation. Each test case includes the steps to perform, the expected outcome.
