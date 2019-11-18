def palindrome(intnum):
    num1 = int(intnum)
    newn = 0
    while intnum > 0:
        n1 = intnum % 10
        intnum //= 10
        newn = newn * 10 + n1
    if num1 == newn:
        print("It is a palindrome number!")
    else:
        print("It is not a palindrome number!")
num = input("Enter a number you want to check:")
while num.isdigit() == False:
    num = input("Enter a integer number:")
intnum=int(num)
palindrome(intnum)