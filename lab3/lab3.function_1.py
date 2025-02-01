# Function1
#1
def convert(grams):
    ounces = 28.3495231 * grams
    print(ounces)
grams = int(input())
convert(grams)

#2
def conv(F):
    C = (5/9)*(F-32)
    print(C)
F = int(input())
conv(F)

#3
def solve(numheads,numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chickens = numheads - rabbits
    print(f"rabbits : {rabbits}",f"chickens : {chickens}")
numheads = int(input())
numlegs = int(input())
solve(numheads,numlegs)

#4
nums = input().split()
l = map(int,nums)
list1 = list(l)

def filter_prime(num):
    if num < 2:
        return False
    cnt = 0
    for i in range(1,num+1):
        if num % i == 0:
             cnt += 1
    if cnt == 2:
        return True
for i in list1:
    num = i
    if filter_prime(num):
        print(num)

#5
from itertools import permutations 
def perma(k):
    perm = permutations(k)
    for i in perm:
        print(i)
k = input()
perma(k)  

#6
def user_str(s):
    for i in range(len(s)-1,-1,-1):
        print(s[i],end = " ")
s = input().split()
user_str(s)

#7 
def has_33(nums):
    for i in range(len(nums)-1):
        if (nums[i]==3 and nums[i+1]==3) :
            return True
    return False
print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))

#8
def spy_game(nums):
    seq = []
    for i in nums:
        if i == 0 and len(seq) < 2:
            seq.append(0)
        elif i == 7 and len(seq) == 2:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))     
print(spy_game([1,7,2,0,4,5,0]))

#9
import math
def vol(r):
    volume = (4/3)*math.pi*(r**3)
    print(volume)
r = int(input())
vol(r)

#10
unq_list = []
def unq(list1):
    for i in list1:
        if i not in unq_list:
            unq_list.append(i)
    return unq_list
list1 = input().split()
print(unq(list1))

unq_list = []
def unq(list1):
    for i in list1:
        if i not in unq_list:
            unq_list.append(i)
    return unq_list
list1 = [1,1,1,1,2,2,3,54,4,1,2,5,5,7]
print(unq(list1))

#11
def palindromee(s):
    return s == s[::-1]
s = input()
if palindromee(s):
    print("PALINDROME")
else:
    print("NO")

#12
def histogram(hist):
    for i in hist:
        print('*'*i)
histogram([4,9,7])

# 13
import random
num = random.randint(1,20)
print("Hello! What is your name?")
name = input()
c = 0
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
while True:
    print("Take a guess.")
    number = int(input())
    if num > number:
        print("Your guess is too low.")
        c += 1
    elif num < number:
        print("Your guess is too high")
        c += 1
    else:
        print(f"Good job, {name}! You guessed my number in {c} guesses!")
        break

























































































