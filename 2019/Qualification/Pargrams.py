#cp template 
import math 

def primeFactor(n):
    n2 = 0
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            n2 = i 
            n = int(n/n2)

    return n,n2

def solve():
    letters =["A","B","C","D","E","F","G","H", "I", "J", "K", "L", "M", "N", "O", "P","Q","R","S","T","U","V","W","X","Y","Z"]
    a = list(map(int, input().split()))
    maxn = a[0]
    length = a[1]
    encryplist = []
    l = list(map(int, input().split()))
    first = primeFactor(l[0])
    second = primeFactor(l[1])
    result =""

    if first[0] in second:
        encryplist.append(first[1])
        encryplist.append(first[0])
    for x in second:
        if x not in encryplist:
            encryplist.append(x)
    
    for k in range(2, length):
        encryplist.append(int(l[k]/encryplist[-1]))

    sortedl = list(sorted(set(encryplist)))

    d = {}
    for t in range(0, 26):
        d[sortedl[t]] = letters[t]

    
    for x in encryplist:
        result += d[x]

    print("Case #"+str(i+1)+": "+ result)

for i in range(int(input())):
    solve()

