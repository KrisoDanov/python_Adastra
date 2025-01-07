def nums(n):
    list = []
    for i in range(1,n+1):
        list.append(i)
        #print(list)

    for x in range(1, n+1):
        print(list)
        list.pop()
        
var = int(input())

nums(var)