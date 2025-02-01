#1
class First:
    def __init__(self,a=""):
        self.a = a
    def getString(self):
        self.a = input()
    def printString(self):
        print(self.a.upper())
s = First()
s.getString()
s.printString()

#2
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
   
class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length**2
s = Shape()
print("by default",s.area())
s1 = Square(12)
print("square: ",s1.area())
#3
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length*self.width)
a = int(input())
b = int(input())
s = Rectangle(a,b)
s.area()
#4 
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print("Coordinates: ",self.x,self.y)
    def move(self,xnew,ynew):
        self.x = xnew
        self.y = ynew
    def dist(self,other_coor):
        return math.sqrt((self.x-other_coor.x)**2+(self.y-other_coor.y)**2)
p1 = Point(3,4)
p2 = Point(5,6)
p1.show()
p2.show()
p1.move(8,6)
p1.show()
print(p1.dist(p2))
#5
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self,amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            print("Current balance: ",self.balance)
        elif amount > self.balance:
            print("Nedostatochno sredstv")
a = BankAccount("Adiya",600)
amount = int(input())
a.deposit(amount)
a.withdraw(1000)
a.withdraw(200)

#6
list1 = [1,2,7,13,26,45]
prime_nums = filter(lambda x:x > 1 and all( x % i !=0 for i in range(2,x)),list1)
print(list(prime_nums))

