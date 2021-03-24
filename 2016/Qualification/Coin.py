#cp template 
import math

def bintobase(num, base):
    return int(bin(num)[2:], base)

def findFactor(num):
    for k in range(2, int(math.sqrt(num))+1):
        if num % k == 0:
            return k
    return 1

def solve():
    data = list(map(int,input().split()))
    length = data[0]
    case = data[1]
    count = 0
    print("Case #"+str(i+1)+": ")
    for x in range(pow(2, length-1)+1, pow(2,length)-1, 2):
        factors = []
        for t in range(2,11):
            f = findFactor(bintobase(x,t))
            if f == 1:
                break
            factors.append(f)
            
        if len(factors) == 9:
            print(bin(x)[2:], end =" ")
            for o in factors:
                print(o, end = " ")
            print()
            count += 1
        if count == case:
            break
        

   

for i in range(int(input())):
    solve()

