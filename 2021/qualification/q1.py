#cp template 


def solve():
    lenth = int(input())
    l = list(map(int, input().split()))
    total = 0
    for k in range(1,lenth):
        j = l.index(k) + 1
        #print(l[j:])
        l = l[:k-1]+ list(reversed(l[(k-1):(j)])) + l[j:] 
        #print(l)
        total = total + j - k + 1
        #print(total)
    print("Case #"+str(i+1)+": "+ str(total))

for i in range(int(input())):
    solve()