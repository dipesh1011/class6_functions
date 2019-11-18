def factorial(num):
    res = 1
    for i in range(1, num + 1):
        res = res * i
    return res

def combination():
    n = int(input("Enter value for 'n':"))
    r = int(input("Enter value for 'r':"))
    combi = factorial(n) / (factorial(r) * factorial(n-r))
    print("The combination is:",combi)

combination()