def sumofnum():
    # sum of two number 
    a= int(input("Enter first number :"))
    b=int(input("enter second number :"))
    print("sum of two number is ",a+b)

def oddev():
    #odd or even 
    n= int(input("Enter the number :"))
    if(n==0):
        print("number is zero")
    elif(n%2==0):
        print("number is even")
    else :
        print("Number is odd")

def fact():
    # factorial 
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial of", num, "is", fact)

def fib():
    #fibonacci numbers 
    c= int(input("enter the number :"))
    d=0 
    e=1
    for i in range(c):
        print(d,end=" ")
        d,e=e,d+e

def strrev():
    #string reverse
    string= input("enter the string : ")
    print("reverse order of string is:",string[::-1])

def palindrome():
    #palindrome check 
    wrd=input("Enter the word: ")
    pld= wrd[::-1]
    if(pld==wrd):
        print("The given word is Palindrome!")
    else:
        print("The given word is not a palindrome !")

def leapyr():
    year= int(input("enter the year:"))
    if((year%4==0 and year%100!=0)or(year%400==0)):
        print("The year is leap year!")
    else:
        print("Not a leap year!")

def armstr():
    num = int(input("Enter a number: "))
    original = num

    digits = len(str(num))

    sum = 0

    while num > 0:
        digit = num % 10          
        sum += digit ** digits    
        num = num // 10           

    if sum == original:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


while(1):
    print("""    ---Menu---
        1. sum of two num 
        2. Odd and even 
        3. Factorial 
        4. Fibonacci
        5. String reverse
        6. palindrome
        7. Leap year
        8. Armstrong number
        9. Exit the program  """)
    optn= int(input("Enter the option from 1 to 9 (9 for exit) : "))
    match optn:
        case 1:
            sumofnum()
        case 2:
            oddev()
        case 3:
            fact()
        case 4:
            fib()
        case 5:
            strrev()
        case 6:
            palindrome()
        case 7:
            leapyr()
        case 8:
            armstr()
        case 9: 
            print("program exited !")
            break
        case _:
            print("invalid!")
   

