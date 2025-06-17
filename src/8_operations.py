#arithmetic operators
# add, subtract, multiply, divide, modulus, exponent, floor division
# +, -, *, /, %, **, //

x=11
y=5

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

#comparision operators compares two values and return boolean value
#<, >, ==, !=, <=, >=
print(x<y)
print(x>y)
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)

#logical operators
# and, or, not
a,b=True,False
print(a and b)
print(a or b)
print(not a)

#assignment operators
# +=, -=, *=, /=
c=5
c+=2 #x=x+2
print(c)
c-=3 #x=x-3
print(c)
c*=2 #x=x*2
print(c)
c/=3 #x=x/3
print(c)

#membership operators
# in, not in
nums=[1,2,3,4]
print(1 in nums)
print(2 not in nums)

#identity operators
# is, is not
x=[1,2,3,4]
y=x
print(x is y)
print(x is not y)