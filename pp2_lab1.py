# Intro
print("hello,world")
print("how are you?")

# Get Started
import sys
print(sys.version)

# Syntax
if 5>2:
  print("Five is greater than two!")
if 5>1:
      print("yes")

# Comments
print("Hello")

#this is comment
"""
This is a comment written 
"""
print("yoy")

# variables
x = 5
y = "John"
print(x)
print(y)
x = 4
x = ("sally")
print(x)
x = str(3)
y = int(3)
z = float(3)
print(x, y, z)
x = 5
y = "John"
print(type(x))
print(type(y))

# legal var names
myvar = "John"
mu_var = 'john'
_my_var = "john"
myVar = "john"
MYVAR = 'john'
myvar2 = 'john'

# multiple values
x, y, z = "orange", "banana", "cherry"
print(x, y, z)
x = y = z = "orange "
print(x)
print(y)
print(z)
fruits =["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# output var
x = "fruits "
y = "are "
z = "perfect"
print(x + y + z)
x = 10
y = 'h'
print(x, y)

# global var
#1)
x = "good"
def func():
    print("my mood is "+x)
func()
#2)
x = "bad"
def wow():
    x="good"
    print("mood is "+x)
wow()
print("mood is "+x)

x = "awesome"
def myfunc():
    global x
    x = "amazing"

myfunc()

print(x)

# Data types
x = {"apple", "banana"}
print(type(x))

y = [2,3]
print(type(y))

# Numbers
x = 2
y = 9.6
z = 8j
print(type(x))
print(type(y))
print(type(z))

import random
print(random.randrange(1,10))

# Casting
x = int(2.8)
y = int("3")
z = str(3.0)
print(z)
print(x+y)

# String
a = """fheuyfieyfiueyfiuey
knflehfoierfoe
jfejfpj"""
print(a)
b = ("kef"
     "kmc")
print(b)

a = "hello,world"
print(a[1])

for i in "adiya":
    print(i)
print(len("adiya"))

h = "you are perfect"
print("you" in h)

txt = "pop"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")