#Funtion as parameter
def sum_numbers(n):
    return sum(n)

def higher_order_function(sum_numbers, x):
    summation = sum_numbers(x)
    return summation
result = higher_order_function(sum_numbers, [1,2,3,4,5])
print(result)

#Function as return value
def square(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))

result = higher_order_function('cube')
print(result(3))

result = higher_order_function('absolute')
print(result(-9))

#Python closure
def add_ten():
    ten = 10
    def add(num):
        return ten + num
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(40))

#Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(greeting):
    def wrapper():
        func = greeting()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())

#Function by implementing decorator
def upprcase_decorator(greeting):
    def wrapper():
        func = greeting()
        uppercase = func.upper()
        return uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())

#Multiple Decorators to a single function
def uppercase_decorator(greeting):
    def wrapper():
        func = greeting()
        uppercase = func.upper()
        return uppercase
    return wrapper

def splitting(greeting):
    def wrapper():
        func = greeting()
        split = func.split()
        return split
    return wrapper

@splitting
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())

#Accepting Parameters in Decorator Functions
def decorator_with_parameters(print_full_name):
    def wrapper(para1, para2, para3):
        print_full_name(para1, para2, para3)
        print('I live in {} '.format(para3))
    return wrapper
@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print('I am {} {}. I love to teach'.format(first_name, last_name, country))

print_full_name('Kamran','Habib','India')

#Map Function
num = [1,2,3,4,5]
def square(x):
    return x ** 2
square_num = map(square, num)
print(list(square_num))

#By putting lambda function
square_num_2 = map(lambda x: x**2, num)
print(list(square_num_2))

#Example 2
num_str = ['1','2','3','4','5']
num_int = map(int, num_str)
print(list(num_int))

#Example 3
name = ['Kamran', 'Reetika', 'Insha', 'Arqam']
def capital(name):
    return name.upper()

capital_name = map(capital, name)
print(list(capital_name))

#Filter Function
#Example 1
num = [1,2,3,4,5,6,7,8,9,10]
def even(num):
    if num % 2 == 0:
        return True
    return False

even_num = filter(even, num)
print(list(even_num))

#Example 2
num = [1,2,3,4,5,6,7,8,9,10]
def odd(num):
    if num % 2 != 0:
        return True
    return False

odd_num = filter(odd, num)
print(list(odd_num))

#Example 3
name = ['Kamran', 'Reetika', 'Insha', 'Arqam']
def length(name):
    if len(name) > 5:
        return True
    return False

length_name = filter(length, name)
print(list(length_name))

name = ['Kamran', 'Reetika', 'Insha', 'Arqam']
def length_less(name):
    if len(name) < 5 or len(name) == 5:
        return True
    return False

length_name_2 = filter(length_less, name)
print(list(length_name_2))

#Reduce Python
#import functools
#num_str = ['1','2','3','4','5']
#def add(x, y):
 #   return int(x) + int(y)

#total = reduce(add, num_str)
#print(total)
