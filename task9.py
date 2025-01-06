
def fac_func(test):

    num = 1
    for i in range(test + 1):
    #print(i)
        if i > 0:
            num *= i
    print(num)


var = int(input())
fac_func(var)
