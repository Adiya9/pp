# Booleans
print(11>2)
print(15==0)
print(2<15)

d = 300
n = 44
if d > n:
    print("right")
else:
    print("noooo")

print(bool('yeep'))
print(bool(15))
print(bool(['a','b']))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))

class fin():
    def __len__(self):
        return 0

m = fin()
print(bool(m))

def func():
    return True

print(func())

def func():
    return False
if func():
    print("da")
else:
    print("net")

x = 1000
print(isinstance(x,int))

# Operators
print(23+65)
print(65*98)
print(69-2000)
print(5896//58)

c = 10
f = 15
c/=5
f&=9
print(c,' ',f)

first = 12
second = 14
print(first!=second)

k = 18
if k<20 and 5<k:
    print("yes")

x = ['ananas','neananas']
y = ['neananas','ananas']
print(x is y)
print(x is not y)

v = [1,2,3,34,5,6]
print(5 in v)

print(12&2)
print(5<<6)

print(100+5*9)

# Lists
myna_list = [56,54,12,1]
print(myna_list,' ',len(myna_list))

l = ['abc',100,True,25.6]
print(l)
print(type(l))

make_list = list(("aj","lo"))
print(make_list)

# Access List Items
myna_list = [56,54,12,1]
print(myna_list[3],myna_list[-2])

longone = [1,2,3,4,5,6,7]
print(longone[1:4])
print(longone[:5])
print(longone[2:])
print(longone[-4:-1])
if 6 in longone:
    print("yeeeeeeeeeees")


#Change List Items
list1 = ['toyoto','lexus','audi']
list1[1] = 'kaidagy lexus BMW is beeest'
print(list1)

t = ["a", "b", "c", "o", "k", "m"]
t[1:3] = ["bl", "w"]
print(t)

t.insert(0,'no')
print(t)

# Add List Items
t = [10,20,30,40]
t.append(50)
print(t)

first = ['a','b','c','d','e']
second = ['f','g']
first.extend(second)
print(first)

h = [1,2,3]
f = (5,6,8)
h.extend(f)
print(h)

# Remove List Items
first = ['a','b','c','d','e']
first.remove('a')
print(first)
first.pop(3)
print(first)
first.pop()
print(first)

listik = ['ear','neck','nose']
del listik[2]
print(listik)

listik.clear()
print(listik)

# Loop Lists 
tizim = [9,8,7,6,5,4,3,2,1]
for i in tizim:
    print(i,end=' ')

tizim = [9,8,7,6,5,4,3,2,1]
for i in range(len(tizim)):
    print(i+1,':',tizim[i])

tizim = [9,8,7,6,5,4,3,2,1]
j = 0
while j<len(tizim):
    print(tizim[j])
    j+=1

listik = ['da','net','nu']
[print(i) for i in listik]


#List Comprehension
vege = ['potato','tomato','cucumber']
new = []
for i in vege:
    if 'o' in i:
        new.append(i)
print(new)

vege = ['potato','tomato','cucumber']
new = [i for i in vege if 'p'in i]
print(new)

j = [1,2,3,7]
new1 = [j[i] for i in range(len(j)) if j[i]<6]
print(new1)

new_one = [i.upper() for i in vege]
print(new_one)

new2 = [i if i == 'potato' else 'or' for i in vege]
print(new2)

# Sort Lists 
li = [23,12,333,21,2,1]
li.sort()
print(li)
li.sort(reverse = True)
print(li)

def function(n):
    return abs(n-50)

list1 = [500,6,4,8,5,4]
list1.sort(key = function)
print(list1)

l = ['wanan','Mandarin','peach']
l.sort()
print()
l.sort(key = str.lower)
print(l)

l.reverse()
print(l)

# Copy Lists
tizim = [1,2,3]
my = tizim.copy()
print(my)

list1 = ['a','b','c']
list2 = list(list1)
print(list2)

list3 = list1[:]
print(list3)


# Join Lists
list1 = [1,2]
list2 = ['al','mo','po']
list3 = list1 + list2 
print(list3)

for i in list2:
    list1.append(i)
print(list1)

list1.extend(list2)
print(list1)

# List Methods
listik = [10,11,12,13,14,15]
print(listik.index(11))

# Tuple
tuple1 = ("s","k","o")
print(tuple1)
print(len(tuple1))

th = ("lolo",)
print(type(th))

#NOT a tuple
th = ("lolo")
print(type(th)) 

tup = ("abc",34,True)
print(tup)

# Access Tuple Items
t = (1,2,3,4,5,6)
print(t[1])
print(t[-1])
print(t[:3])
if 3 in t:
    print("yess")

# Update Tuples
p = (132,273,78,829)
p1 = list(p)
p1[1]=0
p1.append(256999)
p1.remove(78)
p = tuple(p1)
print(p)

new_tuple = ('q','w','e','r')
k = ('t',)
new_tuple+=k
print(new_tuple)

tuplik = (58,69,321,45)
del tuplik

# Unpack Tuples
veges = ('tomato','cucumber','poteto')
(red,green,brown) = veges
print(red,green,brown)

nums = (1,10,100,200,300)
(birlik,ondyk,*zhuzdik) = nums
print(zhuzdik)
print(birlik,ondyk)

# Loop Tuples 
mytuple = (1,2,3,4,5,6,7,8,9)
for i in mytuple:
    print(i)

mytuple = (1,2,3,4,5,6,7,8,9)
for j in range(len(mytuple)):
    print(mytuple[j],end=" ")

mytuple = (1,2,3,4,5,6,7,8,9)
k = 0
while k<len(mytuple):
    print(mytuple[k])
    k+=1

# Join Tuples
tuple1 = ('q','w','e')
tuple2 = (1,2,3)
tuple3 = tuple1+tuple2
tuple4 = tuple1*2
print(tuple3)
print(tuple4)

# Tuple Methods
tuple1 = ('q','w','e','e','e')
print(tuple1.count('e'))
print(tuple1.index('e'))


# Sets
myset = {"kiwi","peach","pear"}
print(myset)

setik = {1,True,2}
print(setik)
print(len(setik))

set1 = {'abc',34,True,'l'}
print(set1)
print(type(set1))

list1 = [1,2,3,3,4]
set1 = set(list1)
print(set1)

# Access set items
setik = {121,144,169}
for i in setik:
    print(i)
print(121 in setik)

# Add Set Items
t = {'a','b','c','d'}
t.add('e')
print(t)

set1 = {'a','a','b'}
set2 = {'c','d','e','e'}
set1.update(set2)
print(set1)

set1 = {'a','a','b'}
list1 = [1,2,3,4]
set1.update(list1)
print(set1)

# Remove set items
set1 = {'a','a','b'}
set1.remove('a')
set1.discard('b')
print(set1)

setik = {9,8,7,6,5,4,3,2,1}
p = setik.pop()
print(p,setik)

setik.clear()
print(setik)

thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)

# Loop Sets 
sett = {1,2,3,4,5,6,7,8,9}
for i in sett:
    print(i)

# Join Sets
_1 = {1,2,3,4}
_2 = {5,5,5,5}
_3 = _1.union(_2) # instead we can use |
print(_3)

set1 = {'a','b','c'}
set2 = {'d','e','f'}
set3 = {1,2,3}
res = set1.union(set2,set3)
print(res)
res = set1 | set2 | set3
print(res)

set1 = {'a','b','c','d'}
set2 = {'d','e','f'}
set3 = set1.intersection(set2) # can use &
set1.intersection_update(set2)
print(set1)
print(set3)

set1 = {"a", "ban", "cherry"}
set2 = {"goog", "micro", "a"}
set3 = set1.difference(set2)
print(set3)

set1 = {"alma", "banan", "vishnya"}
set2 = {"google", "microsoft", "alma"}
set3 = set1.symmetric_difference(set2) # ^
print(set3)

# Dictionaries
dict1 = {1:12,2:24,3:36}
print(dict1)
print(dict1[1])
print(len(dict1))

mydict = {'color':'blue',
          'type':[1,11,111]}
print(mydict)

k = dict(name = '2',ag = '3',l = '4')
print(k)

# Access Items
slovar = {'name':"adiya","age":18,"height":168}
d = slovar.get("height")
print(d)
k = list(slovar.keys())
k1 = list(slovar.values())
print(k,k1)
slovar['name']='nurik'
print(slovar)
print(slovar.items())

# Change Items
slovar = {'name':"adiya","age":18,"height":168}
slovar.update({'height':175})
print(slovar)

# Remove
p = {1:'a',2:'b'}
p.pop(1)
p.popitem()
print(p)

# Loop
for i in slovar:
    print(i,slovar[i])

for i in slovar.values():
    print(i)

for i,j in slovar.items():
    print(i,j)

# Copy
first = {"brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
first_copy = first.copy()
s = dict(first)
print(first_copy)
print(s)

# Nested
classes = {'1A' : {'student':'adika','grade':5},
            '1B' : {'student':'nurik','grade':6}
          }
for i,j in classes.items():
    print(i,j)
    for k in j.values():
        print(k)

# If else
a = 8
b = 5
if a>b:
    print(a)
elif a==b:
    print('equal')
else:
    print(25)

a = 33333
b = 2000000
if not a > b:
  print("a is NOT greater than b")

aa = 65
bb = 200
if b > a:
  pass

# While 
i = 0
while i<14:
    print(i)
    if i==4:
       break
    i+=1

i = 0
while i<3:
    i+=1
    if i==1:
        continue
    print(i)

# For loops
nums = [1,2,3,3]
for i in nums:
    print(i)

for i in 'adiya':
    print(i)
    if i=='i':
        break
    elif i=='d':
        continue

for x in range(1,10,2):
    print(x)

for x in range(3):
  print(x)
else:
  print("Finally ")

list1 = [1,2,3]
list2 = ['a','b','c']
for i in list1:
    for j in list2:
        print(i,j)

for x in ['a','b','c']:
    pass