#1.0.Write a  program to print all natural numbers from 1 to n.(for loop)
""" n=int(input("Enter the number : "))

for i in range(1,n+1):
    print(i)  """


#1.1.Write a  program to print all natural numbers from 1 to n.(while loop)

""" n=int(input("Enter the number : "))
i=1
while i<=n:
    print(i)
    i=i+1 """

#2.0 Write a  program to print all natural numbers in reverse from n to 1(for loop)

""" n=int(input("Enter the number : "))

for i in range(n,0,-1):
    print(i) """

#2.1 Write a  program to print all natural numbers in reverse from n to 1(while loop)

""" n=int(input("Enter the number : "))

while n>=1:
    print(n)
    n=n-1 """

#3.0 Write a  program to print all alphabets from a to z. - using for loop

""" for i in range(65,91):
    print(chr(i),end=' ')
print("\n")
for i in range(97,123):
    print(chr(i),end=' ') """

#3.0 Write a  program to print all alphabets from a to z. - using while loop

# i=65
# while i<91:
#     print(chr(i),end=' ')
#     i=i+1
# print("\n")
# i=97
# while i<123:
#     print(chr(i),end=' ')
#     i=i+1


#4.0 Write a  program to print all even numbers between 1 to 100. - for  loop

# for i in range(1,100+1,1):
#     if i%2==0:
#         print(i,end=' ')

#4.0 Write a  program to print all even numbers between 1 to 100. - while  loop
# i=1
# while i<=100:
#     if i%2==0:
#         print(i,end=' ')
#     i=i+1

#5.0 Write a  program to print all odd number between 1 to 100.(for loop)
# for i in range(1,100+1,1):
#    if i%2!=0:
#        print(i,end=' ')

#5.1 Write a  program to print all odd number between 1 to 100.(while loop)
# i=1
# while i<=100:
#     if i%2!=0:
#         print(i,end=' ')
#     i=i+1

#6. Write a  program to find sum of all natural numbers between 1 to n.

# n=int(input("Enter the number : "))

# sum=0

# for i in range(1,n+1,1):
#     sum=sum+i
# print("Sum of the number : ",sum)


#7. Write a  program to find sum of all even numbers between 1 to n.

# n=int(input("Enter the number : "))
# sum=0
# for i in range(2,n+1,2):
#     sum=sum+i
# print("Sum of even number : ",sum)


#8. Write a  program to find sum of all even numbers between 1 to n.
# n=int(input("Enter the number : "))
# sum=0
# for i in range(1,n+1,2):
#     sum=sum+i
# print("Sum of odd number : ",sum)

#9. Write a  program to print multiplication table of any number.

# number = int(input("Enter the number : "))

# for i in range(1,10+1,1):
#     result=i*number
#     print(i, "X" ,number, " = ",result)


#10. Write a  program to count number of digits in a number.

""" n=int(input("Enter the digits : "))
count=0

while n>0:
    count=count+1
    n=n//10
      
print(count) """

#11. Write a  program to find first and last digit of a number.

""" n = int(input("Enter the digits : "))

last_digit=n%10

print("Last digit is : ",last_digit)

first_digit=n

while first_digit>=10:

    first_digit=first_digit//10

print("First digit is : ",first_digit) """


#12. Write a program to find sum of first and last digit of a number.

""" n = int(input("Enter the digits : "))

last_digit=n%10

print("Last digit is : ",last_digit)

first_digit=n

while first_digit>=10:

    first_digit=first_digit//10

print("First digit is : ",first_digit)

sum=first_digit+last_digit

print("Sum of first and last digit is : ",sum) """

#13.Write a  program to calculate sum of digits of a number.

""" digits=int(input("Enter the digits : "))
n=digits
sum=0

while n!=0:
    remainder=n%10
    sum=sum+remainder
    n=n//10

print("Sum of digits is : ",sum) """


#14. Write a  program to calculate product of digits of a number.

""" 
digits=int(input("Enter the digits : "))
n=digits
sum=1

while n!=0:
    remainder=n%10
    sum=sum*remainder
    n=n//10

print("Product of digits is : ",sum) """


#15. Write a  program to enter a number and print its reverse.

""" digits=int(input("Enter the digits : "))
n=digits

reverse=0
while n!=0:
    remainder=n%10
    reverse=reverse*10+remainder
    n=n//10

print("Revers of digits is : ",reverse) """

#16 . Write a program to check whether a number is palindrome or not.

""" digits=int(input("Enter the digits : "))
n=digits

reverse=0
while n!=0:
    remainder=n%10
    reverse=reverse*10+remainder
    n=n//10

if reverse==digits:
    print("Its palindrome number")

else:
    print("Its not palindrome number") """

#17. Write a  program to print all ASCII character with their values.
""" 
for i in range(1,255+1,1):
    print(chr(i),end=' ') """

#18. Write a  program to find power of a number using for loop.

""" base=int(input("Enter the Base : "))
exponent=int(input("Enter the Exponent : "))

power=1

for i in range(exponent):
    power=power*base
print(power)
 """

#19. Write a  program to find all factors of a number.

""" n=int(input("Enter the number : "))

for i in range(1,n):
    if n % i ==0:
        print(int(i),end=' ') """

#20. Write a  program to calculate factorial of a number.

""" n=int(input("Enter the number : "))

fact=1

for i in range(1,n+1):
    fact=fact*i
print(fact) """

#21. Write a  program to find HCF (GCD) of two numbers.

""" number_1=int(input("Enter the first  number : "))
number_2=int(input("Enter the first  number : "))

n_1=number_1
n_2=number_2

while n_2 != 0:
    remainder=n_1%n_2
    n_1=n_2
    n_2=remainder

gcd=n_1
print("GCD is : ",gcd) """

#22.Write a  program to find LCM of two numbers.

""" number_1=int(input("Enter the first  number : "))
number_2=int(input("Enter the first  number : "))

n_1=number_1
n_2=number_2

while n_2 != 0:
    remainder=n_1%n_2
    n_1=n_2
    n_2=remainder

gcd=n_1

lcm=number_1*number_2//gcd

print("LCM is : ",lcm) """

#23 Write a  program to check whether a number is Prime number or not.

""" n=int(input("Enter the Number for check Prime or not : "))

count=0
for i in range(2,n,1):
    if n%i==0:
        count=count+1
        break;
if(count==0):
    print(n," is prime number")
else:
    print(n," is not prime number")
 """
#24 Write a  program to print all Prime numbers between 1 to n.
""" number=int(input("Enter the Number  : "))

for i in range(2,number,1):
    count=0
    for j in range(2,i,1):
        if i%j==0:
            count=count+1
            break
    if count==0:
        print(i,end=' ') """

#25 Write a  program to find sum of all prime numbers between 1 to n.

""" number=int(input("Enter the Number  : "))
sum=0

for i in range(2,number,1):
    count=0
  
    for j in range(2,i,1):
        if i%j==0:
            count=count+1
            break
    if count==0:
        sum=sum+i
print(sum) """

#26 Write a  program to check whether a number is Armstrong number or not.

""" n=int(input("Enter the Number  : "))

number=n
arm_Strong=0

for i in range(1,number,1):
    remainder=number%10
    arm_Strong=arm_Strong+remainder**3
    number=number//10

if n==arm_Strong:
    print(n," is Armstrong number ")
else:
    print(n," is not  Armstrong number ")
 """

 #27 Write a  program to print all Armstrong numbers between 1 to n.(bug)
""" 
n=int(input("Enter the Number  : "))
for i in range(1,n+1,1):

    nu=i
    arm_Strong=0
    while nu>0:

        remainder=nu%10
        arm_Strong=arm_Strong+remainder**3
        nu=nu//10

    if i==arm_Strong:
        print(i) """

#28 Write a program to check whether a number is Perfect number or not.

""" n=int(input("Enter the Number  : "))
sum=0
for i in range(1,n,1):
    if n%i==0:
        sum=sum+i

if(n==sum):
    print(sum," is Perfect Number ")
else:
    print(sum,"is not Perfect Number ") """

#29 Write a  program to print all Perfect numbers between 1 to n.
""" 
n=int(input("Enter the Number  : "))

for i in range(1,n,1):
    sum=0
    for j in range(1,i,1):

        if i%j==0:
            sum=sum+j

    if(i==sum):
        print(sum) """

#30 Write a program to check whether a number is Strong number or not.

""" num=int(input("Enter the number "))
temp=num
sum=0
while temp!=0:
    fact=1
    remainder=temp%10
    for i in range(1,remainder+1,1):
        fact=fact*i
    sum=sum+fact
    temp=temp//10

if sum==num:
    print(sum," is strong number ")
else:
    print(sum," is not  strong number ") """

#31 Write a  program to print all Strong numbers between 1 to n.

"""num=int(input("Enter the number : "))

 for i in range(1,num+1,1):
    sum=0
    temp=i

    while temp!=0:

        fact=1
        remainder=temp%10
        for j in range(1,remainder+1,1):
            fact=fact*j
        sum=sum+fact
        temp=temp//10

    if sum==i:
        print(i)
 """


#32 Write a  program to print Fibonacci series up to n terms.

""" number=int(input("Enter the Number "))

first_number=0
second_number=1
answer=0

for i in range(1,number,1):
    print(answer)
    first_number=second_number
    second_number=answer
    answer=first_number+second_number
     """







    

    


        
    





















