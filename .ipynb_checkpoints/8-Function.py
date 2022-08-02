#function is a block of code that perform a specific task

#Problem
#You are given two lists of numbers and you need to find totoal of these.

# Tom_expenses_list = [200,300,500]
# jary_expenses_list = [400,700,100]
#
# total = 0
# for i in Tom_expenses_list:
#     total = total + i
# print("The total expense of tom is:",total)
#
# total = 0
# for i in jary_expenses_list:
#     total = total + i
# print("The total expense of jary is:",total)

#problem of above code is that if we have large numbers oflists we requir we repeate these line every time which is very comber some and time cnsuming.


#Correct approch is
def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total
Tom_expenses_list = [200,300,500]
jary_expenses_list = [400,700,100]

Tom_total = calculate_total(Tom_expenses_list)
jary_total =calculate_total(jary_expenses_list)

# print("toms expsnses are : ",Tom_total)
# print("jary expsnses are : ",jary_total)


#proble2: sum of two numbers
def sum(a,b):
    total = a+b
    return total

n = sum(4,5)
# print("The sum of these is :",n)

#proble2: sum of two numbers
# def sum(a,b):
#     print("a",a)
#     print("b",b)
#     total = a + b
#     print("total inside function : ", total)
#     return total
# #named argument
# #n = sum(a=4,b = 5)
# n = sum(b=6,a=4)
# print("The sum of these is :",n)


#Global vs local variables
#Above all varibles belong to local variible cate gory

#Global Variables
#proble2: sum of two numbers
# total = 0
# def sum(a,b):
#     print("a",a)
#     print("b",b)
#     total = a + b
#     print("total inside function : ", total)
#     return total
#named argument
n = sum(b=6,a=4)
# print("Total outside function :",total)

#here total is a global variable outside and local is  inside


#Defalut Arguments

total = 0
def sum(a,b =0 ):#if user cant put value of b it is by default zero
    print("a",a)
    print("b",b)
    total = a + b
    print("total inside function : ", total)
    return total
# named argument
n = sum(a=6)
print("Total outside function :",total)


total = 0
def sum(a,b =0 ):#if user cant put value of b it is by default zero
    """ this triple qutes used for documentation in sytrings."""
    print("a",a)
    print("b",b)
    total = a + b
    print("total inside function : ", total)
    return total
# named argument
n = sum(a=6,b=7)
print("Total outside function :",total)