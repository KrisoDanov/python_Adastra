
def listsum(input):

    list = [2,7,11,15]

    num = 0
    target = 0

    for i in list:
        num = i
        #print(i)
        if target == input:
            #print('Output:', target)
            break
        for x in list:
            #print('This is X:', x)
            target = i + x
            if target == input:
                print('Output:', target)
                print('Indexes are', list.index(i), 'and', list.index(x) )
                break
            else:
                target = 0

input = int(input())

listsum(input)

