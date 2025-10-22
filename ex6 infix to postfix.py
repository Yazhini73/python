operator=set(['+','-','*','/','(',')','^'])
priority={'+':1,'-':1,'*':2,'/':2,'^':3}
def infix_to_postfix(exp):
    stack=[]
    output=''
    for ch in exp:
        if ch not in operator:
            output+=ch
        elif ch=='(':
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[ch]<=priority[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output
exp=input("Enter infix Expression:")
print("Infix Expression:",exp)
print("Postfix Expression:",infix_to_postfix(exp))

            
                
