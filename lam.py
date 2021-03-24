# old way
"""
def remainder(num):
    return num % 2
"""
# Lambda functions are used when you need a functino for a short period of time. Procudes a FUNCTION OBJECT
# this is commonly used when you want to pass a function as part of an argument

# lambda way (Ex 1)
remainder = lambda num: num % 2

print(remainder(5))

# Ex 2
product = lambda x, y: x * y

print(product(2, 3))

# Ex 3
def testfunc(num):
    return lambda x: x * num


result1 = testfunc(10)
result2 = testfunc(1000)

print(result1(9))
print(result2(9))


# filtering with lambda
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

filtered_list = list(filter(lambda num: (num > 7), numbers_list))

print(filtered_list)


# mapping with and without lambda
def addition(n):
    return n + n


# We double all numbers using regular functions
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

numbers = (1, 2, 3, 4)
result = list(map(lambda x: x + x, numbers))
print(result)

# same but use two lists
numbers = (1, 2, 3, 4)
numbers2 = (5, 6, 7, 8)
result = list(map(lambda x, y: x + y, numbers, numbers2))
print(result)