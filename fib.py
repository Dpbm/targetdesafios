memo = {0:0, 1:1}
def fib(i):
    if(i < 0):
        return 0
    elif(memo.get(i) != None):
        return memo[i]

    fib_1 = fib(i-1)
    fib_2 = fib(i-2)

    if(memo.get(i-1) == None):
       memo[i-1] = fib_1
    if(memo.get(i-2) == None):
        memo[i-2] = fib_2

    return fib_1 + fib_2

def find_n(target):
    if(target in {0, 1}):
        print("valor pertence a sequência!")
        return

    counter = 3
    while True:
        fib_value = fib(counter)
        if(fib_value == target):
            print("Valor pertence a sequência")
            return
        elif(fib_value > target):
            print("Valor não pertence a sequência!")
            return

        counter += 1



if __name__ == '__main__':
    target = int(input("Valor que deseja encontrar: "))
    find_n(target)
