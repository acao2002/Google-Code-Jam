#cp template 

def check(num):
    num = str(num)
    l = []
    for i in range (0, -(len(num)), -1):
        if num[i] == "4":
            if i == 0:
                l.append(len(num)-1)
            else:
                l.append(-(i)-1)

    return l 

def findSum(num, l):
    n2 = 0
    for x in l:
        n2 += pow(10,x)
        num -= pow(10,x)
    print(n2, end =" ")
    print(num)
        
def solve():
    num = int(input())
    print("Case #"+str(i+1)+":", end = " ")
    findSum(num, check(num))

for i in range(int(input())):
    solve()

