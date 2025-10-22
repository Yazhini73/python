class Queue:
    def __init__(self):
        self.queue=[]
    def is_empty(self):
        return len(self.queue)==0
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]
    def size(self):
        return len(self.queue)
def is_palindrome(s):
    queue=Queue()
    for char in s:
        queue.enqueue(char)
    while queue.size()>1:
        if queue.dequeue()!=queue.queue[-1]:
            return False
        queue.queue.pop()
    return True
string="radar"
if is_palindrome(string):
    print(f"{string} is palindrome")
else:
    print(f"{string} is not a palindrome")
string="hello"
if is_palindrome(string):
    print(f"{string} is palindrome")
else:
    print(f"{string} is not a palindrome")
    
    
