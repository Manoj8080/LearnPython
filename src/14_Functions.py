# in this we will learn
'''
. how to define a function
. function parameters and arguments
. returning values from functions
'''

# fun difination
'''
def function_name():
    code
'''
def say_hello():
    print("hello world")
say_hello()

def greet(name="guest"):
    print("hello", name)

name=input("enter your name:")
greet(name)

def add(x,y):
    print("sum is: ",x+y)
x=int(input("enter a number"))
y=int(input("enter another number"))
add(x,y)


