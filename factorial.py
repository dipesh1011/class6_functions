def factorial(num):
    res = 1
    for i in range (1,num+1):
        res = res * i
    return res

n1 = int(input("Enter a number to find factorial:"))
print("The factorial of",n1,"is:",factorial(n1))