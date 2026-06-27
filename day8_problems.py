#problem 1 

# n = int(input(" enter a number: "))

# for i in range (1, 11):
#     print(f"{n} x {i} = {n * i} ")

#problem2

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f" hello {name}")

#problem 3

# n = int(input(" enter a number: "))

# i = 1

# while(i<11):
#     print(f"{n} x {i} = {n * i} ")
#     i += 1

# problem 4

# n = int(input("enter number:"))

# for i in range (2, n):
#     if(n%i) == 0:
#         print("number is not prime")
#         break
# else: 
#     print("number is prime")

#problem 5

# n = int(input("enter number:"))
# i = 0  
# sum = 0
# while(i<=n):
#     sum += i
#     i +=1

# print(sum)

#problem 6

# n = int(input("enter number:"))

# product=1
# for i in range(1, n+1):
#     product = product * i

# print(f"factorial of number given is : {product}")
 
#problem 7

'''
for n = 3
  * 
 ***
*****
'''
# n = int(input("enter number:"))
# for i in range (1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")  
#     print("")

#problem 8

'''
for n = 3
* 
***
*****
'''
# n = int(input("enter number:"))
# for i in range (1, n+1):
#     print("*"* i, end="")  
#     print("")

#problem 9
'''
* * *
*   *   for n = 3
* * *
'''

# n = int(input("enter number:"))
# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"*n, end="")
    
#     else:
#         print("*",  end="")
#         print(" "* (n-2), end="")
#         print("*", end="")
    
#     print("")
    
#problem 10

n = int(input("enter number:"))

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")
