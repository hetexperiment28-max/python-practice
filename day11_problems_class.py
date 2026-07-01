#question1

# def greatest(a,b,c):
#     if(a>b) and (a>c):
#         return a
#     if(b>a) and (b>c):
#         return b
#     else :
#         return c
    
# a = 1
# b = 3
# c = 2
# print(greatest(a,b,c))


#problem2 celcius to farenheit
#c/5 = (f-32)/9

# def f_to_c(f):
#     return 5*(f-32)/9


# f = int(input("enter temperature in F: "))
# print(f_to_c(f))


#problem4 sum of n numbers

# def sum(n):
#     if (n==1 or n==0):
#          return 1
#     return sum(n-1) + n

# print(sum(4))

   
#problem5 
"""
***
**
* """
# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(3)

#problem6 

# def inch_to_cm(inch):
#     return inch * 2.54

# n = int(input("enter value in inch: "))
# print(f"value in cm is: {inch_to_cm(n)}")

#problem7 see video 5:30:00 chap8

#problem 8 
##def multiply(n):
    #for i in range(1,11):
        #print(f"{n} x {i} = {n*i}")

#multiply(5)