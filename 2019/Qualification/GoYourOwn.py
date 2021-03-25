#cp template 
def flip(s):
    s = s.replace("S", "T")
    s = s.replace("E", "S")
    s = s.replace("T","E")
    return s 

def solve():
    size = int(input())
    s = input()
    result = flip(s) 
    print("Case #"+str(i+1)+": "+ str(result))

for i in range(int(input())):
    solve()

