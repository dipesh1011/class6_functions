def armstrong(num):
    n1 = 0
    num1 = num
    while(num > 0):
        n = num % 10
        num //= 10
        n1 += n ** 3
    if num1 == n1:
        print("It is a armstrong number!")
    else:
        print("It is not a armstrong number!")

num = int(input("Enter a number you want to check:"))
armstrong(num)