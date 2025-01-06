

def main(n):


        if n < 0 or n > 100:
            print('Number should be in the Range of 1-100')
            return 

        else:
            var = 0
            for i in range(0, n+1):
                var += i
            print(var)

main(10)