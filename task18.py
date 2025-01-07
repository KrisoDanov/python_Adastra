

def wordCounter(x):
    curr = 0
    biggest = 0
    word = ""


    for i in x:
        curr = len(i)
        if curr > biggest:
            biggest = curr
            word = i

    print("The longerst word id:", word)

list = list(map(str, input(). split()))

wordCounter(list)

