# sum of two number 
a= int(input("Enter first number :"))
b=int(input("enter second number :"))
print("sum of two number is ",a+b)

#odd or even 
n= int(input("Enter the number :"))
if(n==0):
    print("number is zero")
elif(n%2==0):
    print("number is even")
else :
    print("Number is odd")

# factorial 
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num, "is", fact)

