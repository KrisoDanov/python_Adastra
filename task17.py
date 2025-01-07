

def pyramidapha(n):
    alph = 65
    for i in range(0, n):
        print("" * (n-i), end=" ")
        for j in range(0, n):
            print(chr(alph), end=" ")
        
        alph += 1
        print()

n = 5
pyramidapha(n)