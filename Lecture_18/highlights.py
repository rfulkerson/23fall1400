# highlights from lecture 18

def isEven(x):
    return x % 2 == 0

def isEmpty(m):
    return len(m) == 0

def repeat(phrase, x):
    for i in range(x):
        print(phrase)

if __name__ == '__main__':
    
    repeat("Hello world!", 5)
    repeat("Goodbye there!", 6)
    repeat(2112, 10)
    repeat([8,16,8], 2)
    
    if isEven(20):
        print("CORRECT: I determined that 20 is even!")
    else:
        print("WRONG: I determined that 20 is odd!")
    a_list = []
    b_list = [10,20,90]
    print("testing a_list", isEmpty(a_list))
    print("testing b_list", isEmpty(b_list))
    print("testing string", isEmpty("Hello there"))
    print("testing empty string", isEmpty(""))
    