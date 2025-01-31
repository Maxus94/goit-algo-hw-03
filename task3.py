num = 3
A=[]
for i in range(1, num+1):
    A.append(i)        
A.reverse()    
B = []
C = []

def hanoi(a, b, c, num):
    global A, B, C
    if num == 0:
        return        
    else:
        hanoi(a, c, b, num - 1)
        print(a, '->', c)
        match a:
            case 'A':
                if c == "C":
                    C.append(A.pop())                    
                else:
                    B.append(A.pop())                    
            case 'B':
                if c == "C":
                    C.append(B.pop())                
                else:
                    A.append(B.pop())                    
            case 'C':
                if c == "A":
                    A.append(C.pop())
                else:
                    B.append(C.pop())
        print(A, B, C)           
        
        hanoi(b, a, c, num - 1)
print(A, B, C)    
hanoi('A', 'B', 'C', num)



    
