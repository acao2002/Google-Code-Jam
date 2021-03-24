def add(l, num):
    while num != 0:
        a = num%10 
        if a not in l:
            l.append(a)
        num = int(num/10)

def found(l):
    return (len(l) == 10)

for i in range(int(input())):
    l = []
    curr = int(input())
    ori = curr
    count = 0
    if curr == 0:
        print("Case #"+str(i+1)+": " +"INSOMNIA")
    else:
        while not found(l):
            count +=1
            curr = ori*count
            add(l, curr)
        print("Case #"+str(i+1)+": " +str(curr))