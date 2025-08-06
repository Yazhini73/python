max_size=5
stack=[]
top=-1
def push(book_title):
    global top
    if top >= max_size -1:
        print("static  overflow can't push more book")
    else:
        top+=1
        stack.append(book_title)
        print(f"Book { book_title} push on to the top")
def pop():
    global top
    if top == -1:
        print(" static is underflow1! can't pop mook")
    else:
        remove=stack.pop()
        print(f"Book { remove} rpopped from the stack")
        top-=1
def peek():
    if top== -1:
        print("stack is empty no book is to peek")
    else:
        print(f"Top  book on the stack is '{stack[top]}'")
def  display():
    if top == -1:
        print("stack is empty")
    else:
        print(" Book is stack ( Top to Bottom)")
        for i in range (top,-1,-1):
            print(f"{i+1}.{stack[i]}")
push("Ice Breaker")
push("Twister")
push("The haunting")
push("Insanity")
push("Omniscience")
push("Good girl")
display()
peek()
pop()
pop()
display()
peek()
