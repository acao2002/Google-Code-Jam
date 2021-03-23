for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    maxele = max(l)
    ret = maxele 
    for x in range(1,maxele):
        totalmoves = 0 
        for item in l:
            totalmoves += (int((item-1)/x) )
        ret = min(ret,(totalmoves+x))
    print("Case #" + str(i+1)+": ", end = " ")
    print(ret)
