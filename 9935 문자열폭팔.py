s=list(input())
boom=list(input())
stack=[]

for i in range(len(s)):
    stack.append(s[i])
    if stack[-1]==boom[-1] and len(stack)>=len(boom):
        if stack[-len(boom):]==boom:
            del stack[-len(boom):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')

            



 
