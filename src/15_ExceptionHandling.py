# ZeroDivisionError
'''num=10
result=num/0
print(result)
'''
# try except block
#try:
    #code that might throe an exception
#except exception type:
    # code to handle exception

'''try:
    num = 10
    result = num / 0
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero")
'''
# else block
try:
    num=int(input("enter a nummber"))
    print(num)
except ValueError:
    print("wrong value entered")
else:
    print("correct")

# finally block
try:
    num = 10
    result = num / 2
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("hehe")
