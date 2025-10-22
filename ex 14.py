class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size
            if index == start_index:
                print("Hash table full!")
                return

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break
        return None

    def delete(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                print(f"Deleted key: {key}")
                return
            index = (index + 1) % self.size
            if index == start_index:
                break
        print(f"Key {key} not found!")

    def display(self):
        for i, item in enumerate(self.table):
            if item is None:
                print(f"Index {i}: Empty")
            else:
                print(f"Index {i}: Key = {item[0]}, Value = {item[1]}")

# Example usage
ht = SimpleHashTable(7)
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("orange", 300)

print("Hash Table:")
ht.display()

print("\nSearch 'banana':", ht.search("banana"))
print("Search 'grape':", ht.search("grape"))

ht.delete("banana")
print("\nAfter deleting 'banana':")
ht.display()
