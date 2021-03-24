def clean(l):
    if len(l) == 1:
        if l[0] == "+":
            l = ""
    else:
        if l[-1] == "+":
            l = l[:-1]
            l = clean(l)

    return l 

def flip(l):
    l = l.replace("+","x")
    l = l.replace("-","+")
    l = l.replace("x","-")
    return l
    
for i in range(int(input())):
    s = input()
    count = 0 
    while len(s)> 0:
        s = clean(s)
        s = flip(s)
        count +=1 
    print("Case #"+str(i+1)+": "+ str(count-1))