

def pyramid(r):
    for i in range(r):
        print(" "*(r-i),'*'*(i*2+1))

var = int(input())
pyramid(var)