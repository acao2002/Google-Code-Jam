

for i in range((int(input()))):
    max, s = input().split()
    max = int(max)
    audi = 0 
    result = 0 
    for k in range(max+1):
        if k > audi:
            h = k - audi
            result += h
            audi = k
        audi += int(s[k])
    print("Case #" + str(i+1)+": ", end = " ")
    print(result)
