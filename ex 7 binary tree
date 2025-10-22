class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to build the tree from user input (recursive)
def build_tree():
    data = input("Enter node value (or 'None' for no node): ")
    if data.lower() == 'none':
        return None

    node = Node(data)
    print(f"Enter left child of {data}")
    node.left = build_tree()
    print(f"Enter right child of {data}")
    node.right = build_tree()
    return node

# Preorder Traversal: Root → Left → Right
def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

# Inorder Traversal: Left → Root → Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

# Postorder Traversal: Left → Right → Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')


print("Build the binary tree:")
root = build_tree()
print("\nPreorder Traversal:")
preorder(root)

print("\nInorder Traversal:")
inorder(root)

print("\nPostorder Traversal:")
postorder(root)
