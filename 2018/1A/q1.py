#cp template 

def checkCol(l, d, total):
    cols = len(l[0])
    factor = int(total/d)
    count = 0
    c = 0 
    i = 0
    cutl = []
    while c < d and i < cols:
        for s in l: 
            if s[i] == "@":
                count+=1
        if count > factor:
            break
        if count == factor: 
            count = 0 
            c+=1
            cutl.append(i)
        i+=1

    if c == d:
        return cutl
    else:
        return []

def checkRow(l, d, total):
    dl = []
    factor = int(total/d)
    count = 0
    c = 0
    Rows = len(l)
    tl = []
    for s in l: 
        count+= s.count("@")
        tl.append(s)
        if count == factor:
            count = 0 
            c+=1
            dl.append(tl)
            tl =[]
        if count > factor:
            break
    if c == d:
        dl.pop()
        return dl 
    else: 
        return []


def findTotal(l):
    count = 0
    for s in l:
        count += s.count("@")
    return count 

def qcheck(total, d1 , d2):
    return total %(d1*d2) == 0


def solve():
    val = 0
    out = ""
    result = True
    l = []
    inpl = list(map(int, input().split()))
    rows = inpl[0]
    d1 = inpl[2]+1
    d2 = inpl[3]+1
    for r in range(rows):
        l.append(input())
    total = findTotal(l)
    if qcheck(total, d1, d2):
        val = int(total/(d1*d2))
        if total == 0:
            result = True
        else:
            dl = checkRow(l, d1, total)
            if not dl:
                result = False
            else:
                dl2 = checkCol(l, d2, total)
                print(dl2)
                if dl2:
                    for item in dl:
                        pass
                else:
                    result == False

    if result:
        out = "POSSIBLE"
    else: 
        out = "IMPOSSIBLE"

    print("Case #"+str(i+1)+": "+ str(out))

for i in range(int(input())):
    solve()