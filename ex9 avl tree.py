class Student:
    def __init__(self, enroll_id, name):
        self.enroll_id = enroll_id
        self.name = name

    def __str__(self):
        return f"{self.enroll_id}: {self.name}"


class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, node, student):
        if not node:
            return Node(student)
        if student.enroll_id < node.student.enroll_id:
            node.left = self.insert(node.left, student)
        elif student.enroll_id > node.student.enroll_id:
            node.right = self.insert(node.right, student)
        else:
            return node # duplicate IDs not allowed

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)

        # Balance tree
        if balance > 1 and student.enroll_id < node.left.student.enroll_id:
            return self.right_rotate(node)
        if balance < -1 and student.enroll_id > node.right.student.enroll_id:
            return self.left_rotate(node)
        if balance > 1 and student.enroll_id > node.left.student.enroll_id:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and student.enroll_id < node.right.student.enroll_id:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

   

    def search(self, node, enroll_id):
        if not node or node.student.enroll_id == enroll_id:
            return node
        if enroll_id < node.student.enroll_id:
            return self.search(node.left, enroll_id)
        return self.search(node.right, enroll_id)

    def inorder(self, node):
        return self.inorder(node.left) + [node.student] + self.inorder(node.right) if node else []

    def count(self, node):
        if not node:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)


# Example usage:
avl = AVLTree()
root = None

students = [
    Student(1001, "Alice"),
    Student(1005, "Bob"),
    Student(1003, "Charlie"),
    Student(1002, "David"),
    Student(1004, "Eve"),
]

for s in students:
    root = avl.insert(root, s)

print("Students enrolled (in order):")
for student in avl.inorder(root):
    print(student)

found = avl.search(root, 1003)
print("\nSearch for student with ID 1003:")
print(found.student if found else "Not found")



print("\nTotal students enrolled:", avl.count(root))
