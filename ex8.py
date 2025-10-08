class Node:
    def __init__(self, key):
        self.key = key            # Node value
        self.left = None          # Left child
        self.right = None         # Right child
        self.height = 1           # Height of the node (needed for balancing)

class AVLTree:
    # Get height of node or 0 if None
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Get balance factor: height(left) - height(right)
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right rotate subtree rooted with z
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    # Left rotate subtree rooted with z
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    # Insert key in subtree rooted with node and balance tree
    def insert(self, node, key):
        # Step 1: Normal BST insertion
        if not node:
            print(f"Inserted {key}")
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Step 2: Update height of this ancestor node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Step 3: Get the balance factor to check if this node became unbalanced
        balance = self.get_balance(node)

        # Step 4: If unbalanced, then balance the tree
        # Case 1 - Left Left
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Case 2 - Right Right
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Case 3 - Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 4 - Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Find node with smallest key (used in deletion)
    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Delete key from subtree rooted with node and balance tree
    def delete(self, node, key):
        # Step 1: Standard BST delete
        if not node:
            print(f"{key} not found for deletion.")
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # Node with only one child or no child
            print(f"Deleted {key}")
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children: get inorder successor (smallest in right subtree)
            temp = self.min_value_node(node.right)
            node.key = temp.key  # Copy successor's value to this node
            node.right = self.delete(node.right, temp.key)  # Delete successor

        # Step 2: Update height
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Step 3: Get balance factor
        balance = self.get_balance(node)

        # Step 4: Balance the node if needed
        # Left Left
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Left Right
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Right Left
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Search key in AVL tree
    def search(self, node, key):
        if not node:
            print(f"{key} not found.")
            return False
        if key == node.key:
            print(f"Found {key}")
            return True
        elif key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    # Inorder traversal (returns sorted keys)
    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.key] + self.inorder(node.right)

    # Count total nodes in tree
    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)


# Usage example
avl = AVLTree()
root = None

# Insert keys
for key in [10, 20, 5, 4, 15, 25]:
    root = avl.insert(root, key)

print("\nInorder traversal:", avl.inorder(root))
print("Total nodes:", avl.count_nodes(root))

# Search for keys
avl.search(root, 15)
avl.search(root, 99)

# Delete a key
root = avl.delete(root, 20)
print("\nInorder traversal after deletion:", avl.inorder(root))
print("Total nodes after deletion:", avl.count_nodes(root))

# Try deleting non-existent key
root = avl.delete(root, 100)
