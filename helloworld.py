import os, sys, random, mymodule as mymod, platform, datetime, math, json, re, matplotlib, matplotlib.pyplot as plt, numpy as np, mysql.connector, pymongo, requests
import camelcase

#to import parts from a module
#from mymodule import person1



print(sys.version)






print("Hello, World!")





if 5 > 2:
	print("5 is greater than 2!")

"""
if 5 > 2:
print("5 is greater than 2!")

if 5 > 2:, statistics
 print("5 is greater than 2!")
        print("5 is greater than 2!")
 """







x = 5
y = "Hello, World!" #Another inline comment







#This is a comment.
#print("Hello, World!")
print("unexecuted code before this")

#This is a comment
#written in
#more than just one line
print("muliple single line comments added before this")

"""
This is a comment
written in
more than just one line
"""
print("multiline string (triple quotes) added before this")







w = 0.5
x = 5
y = "John"
print(w)
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" #x is now of type str
# is the same as
x = 'Sally'
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))


a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "lekker"
print(x, y, z)

x = "Python "
y = "is "
z = "nice"
print(x + y + z)

x = 5
y = 10
print(x + y)

# x = 5
# y = "John"
# print(x + y)

x = 5
y = "John"
print(x, y)


x = "so cool"

def myfunc():
  print("Python is " + x)

myfunc()


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
  global x
  x = "brilliant"

myfunc()

print("Python is " + x)


x = "wow"

def myfunc():
  global x
  x = "amazing"

myfunc()

print("Python is " + x)







"""
Data types:
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType
 """

x = 5
x = "Hello World"
x = 20.4
x = 1j
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
x = {"name" : "John", "age" : 36}
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
x = True
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))
x = None
print(type(x))

x = 1
y = 356562345435342734023749723422554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

x = 1.123789523642384629837432473284723748932749827349879423
y = 1.0
z = -35.59290348
print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

print(random.randrange(1, 100))








print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])







a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.replace("H", "J"))
print(a.split(","))

a = "   Hello, World!  	"
print(a.strip())







a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)







age = 36
txt = f"My name is John, I am {age}"
print(txt)

age = 36
txt = f'My name is John, I am {age}'
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {40 * 12} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

#This example erases one character (backspace):
txt = "Hello W\b\b\b\borld!"
print(txt)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

txt = "this converts the first character to upper case"
print(txt.capitalize())

txt = "This Converts string into Lower case"
print(txt.casefold())

txt = "banana"
x = txt.center(20)
print(x)

txt = "I love apples, apple are my favorite fruit. Aah apples, oh apples!!!"
x = txt.count("apple")
print(x)

txt = "My name is Ståle"
print(txt)
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "Uhm, Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "Welcome to my world"
x = txt.title()
print(x)

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  89}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

txt = "ok, THIS IS NOW!"
x = txt.isupper()
print(x)








print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
print(bool(15.36))
print(bool(True))
print(bool(''))
print(bool(0))
print(bool(None))
print(bool(False))
print(bool([]))
print(bool(()))
print(bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))








"""
Operations:
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
 """
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#Python Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#Python Membership Operators
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

#Python Bitwise Operators
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(3 << 2)
print(8 >> 2)

#BODMAS
print((6 + 3) - (6 + 3))






"""
List []: ordered and changeable. any data types. Allows duplicates.
Tuple (): ordered and unchangeable. any data types. Allows duplicates.
Set {}: unordered, unchangeable*, and unindexed. any data types. No duplicates.
Dict {key: val}: ordered** and changeable. any data types. No duplicates.
 """

#list
print('---lists []---')
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", 26, 234.43, True, "apple", None]
print(thislist[4])

print(len(thislist))

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
newlist = thislist[2:5]
print(newlist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
print(thislist)
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
  print('Nope')
if "banana" in thislist:
  print("Yes, 'banana' is in the fruits list")
else:
  print('Nope')
if "watermelon" in thislist:
  print("Yes, 'watermelon' is in the fruits list")
else:
  print('Nope, no watermelon')

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["kiwi", "orange"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ("kiwi", "orange")
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = {"kiwi", "orange"}
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = {"a":"kiwi", "b":"orange"}
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for x in ["apple", "banana", "cherry"]:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(i)
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(i)
  print(thislist[i])
  i = i + 1

#shortest syntax for looping through lists
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "watermelon", "litchi", "pawpaw"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if "e" in x]
print(newlist)

newlist = [x for x in fruits if "w" in x]
print(newlist)

newlist = [x for x in fruits if (x != "apple" and x != "banana")]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = [x[0].upper() + ' for ' + x.title() for x in fruits]
print(newlist)

print(fruits)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "watermelon", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#3 ways to make a copy of a list
thislist = ["bmw", "audi", "cherry", "volvo", "ford"]
print('thislist orig')
print(thislist)
thisNewList = thislist
print('thisNewList is thislist BY REF')
print(thisNewList)
thisNewList.remove("audi")
print('thisNewList with remove audi')
print(thisNewList)
myEvenNewerlist = thislist.copy()
print('myEvenNewerlist is thislist BY COPY')
print(myEvenNewerlist)

thislist = ["apple", "banana", "cherry"]
print(thislist)
mylist = list(thislist)
mylist.remove("banana")
print(mylist)

thislist = ["apple", "banana", "cherry"]
print(thislist)
mylist = thislist[:]
mylist.remove("banana")
print(mylist)

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3, "b"]
list1.extend(list2)
print(list1)
print(list1.count("b"))








#tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#is a tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
print(thistuple)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple)
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del thistuple

#print(thistuple) #this will raise an error because the tuple no longer exists
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
print(len(fruits))
mytuple = fruits * 3
print(mytuple)
print(len(mytuple))








#set
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"abc", 34, True, 40, "male"}
print(set1)

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(thisset)
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ("kiwi", "orange")
thisset.update(mylist)
print(thisset)

#does raise error if not existing
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


#does not raise error if not existing
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()
print(thisset)
print(x + ' was removed')

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set5 = {True, False}
myset = set1.union(set2, set3, set4, set5)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set5 = {True, False}
myset = set1 | set2 | set3 | set4 | set5
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3, "b"}
set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = ("google", "microsoft", "apple")
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = ["google", "microsoft", "apple"]
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = ("google", "microsoft", "apple")
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = ["google", "microsoft", "apple"]
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = ("google", "microsoft", "apple")
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = ["google", "microsoft", "apple"]
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)







#dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "fuel": 4.7,
  "real": False
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colorsList": ["red", "white", "blue"],
  "colorsSet": {"red", "white", "blue"},
  "colorsTubles": ("red", "white", "blue")
}
print(thisdict)
print(type(thisdict))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
y = thisdict.get("brand")
print(x)
print(y)

print(thisdict.keys())
print(thisdict.values())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

x = thisdict.items()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary: " + thisdict["model"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["year"] = 2018
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.update({"color": "red"})
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "color": "blue",
  "year": 1964
}
print(thisdict)
thisdict.update({"color": "red"})
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
del thisdict
#print(thisdict) # no longer exists

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.clear()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)

car = {
  "brand": "Ford",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
print(car)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

print(myfamily["child2"]["name"])
print(myfamily['child2']['name'])

for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])

"""
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
 """



a = 33
b = 200
if b > a:
  print("b is greater than a")

"""
#error!
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
 """

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

x = 41
#x = 18
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# if with no content
a = 33
b = 200
if b > a:
  pass



i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 33, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(8):
  if x == 3 or x == 5:
    continue
  print(x)
else:
  print("Finally finished!")
  print("Finally finished!")

for x in range(8):
  if x == 3 or x == 5:
    break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass



#functions
def my_function():
  print("Hello from a function")
my_function()

#args
def my_function(fname):
  print(fname + " Lastname")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

"""
#error
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil")
 """

#*args
def my_function(*kids):
  print (kids)
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#kwargs
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#**kwargs
def my_function(**kid):
  print(kid)
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#default parameter
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)
my_function(["apple", "banana", "cherry"])

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

def myfunction():
  pass

def my_function(x, /):
  print(x)
my_function(3)

def my_function(x):
  print(x)
my_function(x = 3)

"""
#error
def my_function(x, /):
  print(x)
my_function(x = 3)
 """

def my_function(*, x):
  print(x)
my_function(x = 3)

def my_function(x):
  print(x)
my_function(3)

"""
#error
def my_function(*, x):
  print(x)
my_function(3)
 """

#Any argument before the /, are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, d = 8, c = 7)

#recursion
def tri_recursion(k):
  if(k > 0):
    print('k is ' + str(k))
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results:")
tri_recursion(6)




#lambda - small anonymous function
#lambda arguments : expression
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 7))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
print(mydoubler(62))
print(mydoubler(72))

def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))



#arrays
cars = ["Ford", "Volvo", "BMW"]
print(cars)
x = cars[0]
print(x)
cars[0] = "Toyota"
print(cars)
x = len(cars)
print(x)
for x in cars:
  print(x)
cars.append("Honda")
cars.append("Audi")
print(cars)
cars.pop(1)
print(cars)
cars.remove("Honda")
print(cars)
cars.reverse()
print(cars)




#Classes and Objects
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 24)
print(p1.name)
print(p1.age)
p2 = Person("Yatish", 36)
print(p2.name)
print(p2.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()

class Person:
  pass



#inheritence
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()
print(type(x))

class Student(Person):
  def __init__(self, fname, lname, year):
    #call the parents __init__
    #Person.__init__(self, fname, lname)
    #inherits parent methods and properties
    super().__init__(fname, lname)
    #add properties etc.
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

  def printname(self):
    print("Welcome", self.firstname, self.lastname)

x = Student("Mike", "Olsen", 2019)
x.printname()
x.welcome()
print(type(x))



#Iterators
#Lists, tuples, dictionaries, and sets are all iterable objects
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)

mystr = "banana"
for x in mystr:
  print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#print(next(myiter)) #error because 21 is out of range



#Polymorphism
x = "Hello World!"
print(len(x))

mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

thisdict = {
  "isSuperCar": True,
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Drive!")
class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Sail!")
class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object
for x in (car1, boat1, plane1):
  x.move()

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Move!")
class Car(Vehicle):
  pass
class Boat(Vehicle):
  def move(self):
    print("Sail!")
class Plane(Vehicle):
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()



#scopes
def myfunc():
  x = 300
  print(x)
myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()
# not available
#print(x)

x = 300
def myfunc():
  print(x)
myfunc()
print(x)

x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)

def myfunc():
  global x
  x = 300
myfunc()
print(x)

x = 300
print(x)
def myfunc():
  global x
  x = 200
myfunc()
print(x)

def myfunc1():
  x = "Jane"
  print(x)
  def myfunc2():
    nonlocal x
    x = "Jill"
  myfunc2()
  return x
print(myfunc1())




#modules
#prints all available modules
#help('modules')

mymod.greeting("Jonathan")

a = mymod.person1["age"]
b = mymod.person1["country"]
print(a)
print(b)
print(mymod.something)
print(mymod.__name__)
print(mymod.__package__)
print(mymod.__spec__)
x = dir(mymod)
print(x)

x = platform.system()
print(x)

x = dir(platform)
print(x)




# dates
x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(1988, 6, 27)
print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%Y"))
print(x.strftime("%c"))
print(x.strftime("%U"))




#Python Math
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

x = abs(-7.25)
print(x)

x = pow(4, 3)
print(x)

x = math.sqrt(64)
print(x)
print(int(x))
print(type(int(x)))
print(type(x))

x = math.ceil(1.3)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

x = math.pi
print(x)
print(f"{x:.50f}")
print(f"{x:.100f}")



#json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
x =  '{ "name":"John", "age":30, "city":"New York", "extra": ["a","b","c"], "properties": {"a":1, "b":2}}'
print(x)
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(type(y))
print(y["name"])
print(y["city"])
print(y["age"])
print(y["extra"])
print(y["properties"])

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print(x)
print(type(x))
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
print(type(y))

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "z": "Some Z text",
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ],
}
print(json.dumps(x))
print(json.dumps(x, indent=2, separators=(". ", " = "), sort_keys=True))




#regex
# findall
# search
# split
# sub
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("ai", txt)
y = re.findall("Portugal", txt)
print(x)
print(y)

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, maxsplit=1)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "-", txt)
print(txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "-", txt, count=2)
print(x)

txt = "The rain in Spain causes pain and not gain"
x = re.search("ai", txt)
print(x) #this will print an object

txt = "The rain in Spain causes pain and not gain"
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())



#pip
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))



#try except else finally
print('try except')
#print(abc)
try:
  print(abc)
except:
  print("An exception occurred")

try:
  print(abc)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
  #print(abc)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  print(abc)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt")
  print('file opened')
  try:
    f.write("Lorum Ipsum")
    print('written')
  except:
    print('exception logged. Something went wrong when writing to the file')
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

"""
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
 """
"""
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
 """




#user input
#3.6
#commented to continue runnning in VS code runner
"""
username = input("Enter username:")
print("Username is: " + username)
 """
#2.7
# username = raw_input("Enter username:")
# print("Username is: " + username)
print('something else')
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)



#Python String Formatting
txt = f"The price is 49 dollars"
print(txt)

price = 69
txt = f"The price is {price} dollars"
print(txt)

price = "one hundred"
txt = f"The price is {price} dollars"
print(txt)

txt = f"The price is {30+25} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {95:.2f} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
  return x * 0.3048
txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price = 69550000
txt = f"The price is {price:,} dollars"
print(txt)

txt = f"We have {49:<8} chickens."
print(txt)

txt = f"We have {49:^8} chickens."
print(txt)

txt = f"The binary version of 5 is {5:b}"
txt = f"The binary version of 64 is {64:b}"
txt = f"The Unicode character of 199 is {199:c}"
print(txt)

txt = f"The Hexadecimal version of 255 is {255:x}"
print(txt)

txt = f"You scored {0.25:%}"
print(txt)

#Or, without any decimals:
txt = f"You scored {0.25:.0%}"
print(txt)

price = 49
product = 'apples';
txt = "The price is {} dollars for {}"
print(txt.format(price, product))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
print(myorder.format(price, quantity, itemno))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))



'''
#File Handling
#f = open("demofile.txt")
#same as above
print(sys.path[0])

f = open("demofile.txt", "rt")
print(f.read())

f = open("demofile.txt", "rt")
print(f.read(5))

f = open("demofile.txt", "rt")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "rt")
for x in f:
  print(x)

#best practice
f = open("demofile.txt", "rt")
print(f.readline())
f.close()

if os.path.exists("temp.txt"):
  f = open("temp.txt", "rt")
  print(f.read())
  #os.remove("temp.txt")



f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#f = open("mybrandnewfile.txt", "x")
#f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())



if os.path.exists("temp.txt"):
  os.remove("temp.txt")
else:
  print("The file does NOT exist")

if os.path.exists("myfolder"):
  os.rmdir("myfolder")
else:
  print("The folder does NOT exist")
'''



#matplotlib
print(matplotlib.__version__)
#print(datetime.__version__)

# plt.plot(1, 2)
# plt.show()

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
# plt.plot(xpoints, ypoints)
# plt.show()

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])
# plt.plot(xpoints, ypoints)
# plt.show()

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])
# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(xpoints, ypoints)
# plt.show()

# ypoints = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoints)
#plt.show()
#plt.show()

# ypointsa = np.array([3, 8, 1, 10])
# ypointsb = np.array([2, 5, 7, 12])
# ypointsc = np.array([9, 14, 3, 6])
# ypointsd = np.array([1, 4, 2, 17])
# ypointse = np.array([18, 9, 11, 3])
# ypointsf = np.array([12, 11, 20, 1])
# plt.plot(ypointsa, marker = 'o')
# plt.plot(ypointsb, marker = '*')
# plt.plot(ypointsc, marker = '+')
# plt.plot(ypointsd, marker = 'D')
# plt.plot(ypointse, marker = 'D')
# plt.plot(ypointsf, marker = '_')
# plt.show()

# ypointsa = np.array([3, 8, 1, 10])
# ypointsb = np.array([2, 4, 11, 1])
# ypointsc = np.array([7, 1, 5, 3])
# ypointsd = np.array([10, 13, 9, 6])
# ypointse = np.array([14, 4, 2, 5])
# plt.plot(ypointsa, 'o-r')
# plt.plot(ypointsb, 'o:g')
# plt.plot(ypointsc, 'o--b')
# plt.plot(ypointsd, 'o-.y', ms = 20, mec = 'r', mfc = 'c')
# plt.plot(ypointse, marker = 'o', ms = 20, mec = '#00ff00', mfc = '#ff0000')
# plt.show()

# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linewidth = '20.5')
# plt.show()

# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()

# stopped doing code copy at Matplotlib Line

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 300, 230])
# plt.plot(x, y, marker = 'o')
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'sans-serif','color':'darkred','size':15}
# font3 = {'family':'monospace','color':'green','size':30}
# plt.title("Sports Watch Data", fontdict = font3, loc = 'left')
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font1)
# plt.grid(color = '#05fa91', linestyle = ':', linewidth = 3, axis = 'y')
# plt.show()
# plt.savefig(sys.path[0] + "/myplot.png")

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.show()

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 1, 1)
# plt.plot(x,y)
# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 1, 2)
# plt.plot(x,y)
# plt.show()

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(3, 3, 1)
# plt.title("SALES")
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(3, 3, 2)
# plt.title("INCOME")
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(3, 3, 3)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(3, 3, 4)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(3, 3, 5)
# plt.plot(x,y)
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(3, 3, 6)
# plt.plot(x,y)
# plt.suptitle("MY SHOP")
# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)
# plt.show()

# #day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y, color = '#00ff0066')
# #day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y, color = '#0000ff66')
# #day two, the age and speed of 15 cars:
# x = np.array([5,7,1,1,17,6,5,2,14,12,10,20,18,2,19])
# y = np.array([50,115,100,98,69,74,88,107,111,83,73,96,86,64,117])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
# plt.scatter(x, y, color = '#ff000066')
# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
# plt.scatter(x, y, c=colors)
# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# plt.scatter(x, y, c=colors, cmap='viridis')
# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# # plt.scatter(x, y, c=colors, cmap='viridis')
# # plt.scatter(x, y, c=colors, cmap='Accent')
# # plt.scatter(x, y, c=colors, cmap='Dark2')
# # plt.scatter(x, y, c=colors, cmap='Pastel1')
# # plt.scatter(x, y, c=colors, cmap='PiYG')
# # plt.scatter(x, y, c=colors, cmap='gist_earth')
# # plt.scatter(x, y, c=colors, cmap='gist_rainbow')
# # plt.scatter(x, y, c=colors, cmap='inferno')
# # plt.scatter(x, y, c=colors, cmap='prism')
# # plt.scatter(x, y, c=colors, cmap='nipy_spectral')
# # plt.scatter(x, y, c=colors, cmap='seismic')
# # plt.scatter(x, y, c=colors, cmap='twilight_shifted')
# # plt.scatter(x, y, c=colors, cmap='cubehelix')
# # plt.scatter(x, y, c=colors, cmap='cividis')
# plt.scatter(x, y, c=colors, cmap='Greys')
# plt.colorbar()
# plt.show()


# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# plt.scatter(x, y, c=colors, cmap='Greys', s=sizes, alpha=0.5)
# plt.show()

# x = np.random.randint(200, size=(200))
# y = np.random.randint(200, size=(200))
# print(x)
# print(y)
# colors = np.random.randint(200, size=(200))
# print(colors)
# sizes = 10 * np.random.randint(200, size=(200))
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='nipy_spectral')
# plt.colorbar()
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x,y)
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.barh(x, y)
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "red")
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "hotpink")
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, color = "#4CAF505E")
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, width = 1, color = "#4EAF50")
# plt.show()

# x = np.array(["A", "B", "C", "D", "E", "F", "G", 'H'])
# y = np.array([3, 8, 1, 10, 0, 4, 9, 7])
# plt.barh(x, y, height = 0.5)
# plt.show()

# x = np.random.normal(1000, 10, 500)
# print(x)
# plt.hist(x)
# plt.show()

# y = np.array([1,2,3])
# #x/sum(x)
# #1/6
# #2/6
# #3/6
# plt.pie(y)
# plt.show()

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels)
# plt.show()

# y = np.array([5, 35, 25, 25, 15])
# mylabels = ['Watermelon', "Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels, startangle = 90)
# plt.show()

# y = np.array([35, 25, 25, 15, 5, 20, 25])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates", "Peach", "Mango", "Oranges"]
# myexplode = [0.2, 0, 0.6, 0, 0.1, 0, 0.3]
# myexplode = [0.1,0.2,0.3,0.4,0.5,0.6, 0.7]
# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
# plt.show()

# y = np.array([35, 25, 25, 5, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates", "Mango"]
# mycolors = ["black", "hotpink", "b", "#4CAF50", "c"]
# plt.pie(y, labels = mylabels, colors = mycolors)
# plt.show()

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels)
# plt.legend()
# plt.show()

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y, labels = mylabels)
# plt.legend(title = "Four Fruits:")
# plt.show()



# MySQL
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm"
# )
# print(mydb)

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

# to check it does exist
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mydatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

# print(mydb)

#error as it does not exists
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mydatabase2"
# )
# print(mydb)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE products (name VARCHAR(100), description VARCHAR(255))")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE reviews (id INT AUTO_INCREMENT PRIMARY KEY, comment VARCHAR(255), recommendation VARCHAR(255))")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Amy", "Sunbird 132")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT name FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers order by id DESC")
# myresult = mycursor.fetchone()
# print(myresult)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers WHERE name ='Amy'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# escape / Prevent SQL Injection
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers WHERE address = %s"
# addr = ("Yellow Garden 2", )
# mycursor.execute(sql, addr)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers WHERE address LIKE CONCAT('%', %s, '%')"
# addr = ("way", )
# mycursor.execute(sql, addr)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "DELETE FROM customers WHERE name = 'Hannah'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "DELETE FROM customers WHERE name = %s"
# addr = ("Peter", )
# mycursor.execute(sql, addr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "DROP TABLE reviews"
# mycursor.execute(sql)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "DROP TABLE IF EXISTS reviews"
# mycursor.execute(sql)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers LIMIT 3")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

#join
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "SELECT \
#   customers.name AS customer, \
#   customers.address AS address, \
#   products.name AS product, \
#   products.description AS description \
#   FROM customers \
#   INNER JOIN products ON customers.product_id = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(len(myresult))
# for x in myresult:
#   print(x)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "SELECT \
#   customers.name AS customer, \
#   customers.address AS address, \
#   products.name AS product, \
#   products.description AS description \
#   FROM customers \
#   LEFT JOIN products ON customers.product_id = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(len(myresult))
# for x in myresult:
#   print(x)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Dox!mYati5hm",
#   database="mypythondatabase"
# )
# mycursor = mydb.cursor()
# sql = "SELECT \
#   customers.name AS customer, \
#   customers.address AS address, \
#   products.name AS product, \
#   products.description AS description \
#   FROM customers \
#   RIGHT JOIN products ON customers.product_id = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(len(myresult))
# for x in myresult:
#   print(x)




# MongoDB
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# print(myclient.list_database_names())

"""
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
else:
  print("The database does not exist.")
 """

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# print(mydb.list_collection_names())

"""
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
 """

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase2"]
# mycol = mydb["customers"]
# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)
# mydict = { "name": "Peter", "address": "Lowstreet 27" }
# x = mycol.insert_one(mydi
# ct)
# print(x.inserted_id)

# myclient = pymongo.MongoClient("mongodb://localhost:12345/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)
# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)
# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# x = mycol.find_one()
# print(x)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# for x in mycol.find():
#   print(x)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#   print(x)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# for x in mycol.find({},{ "address": 0 }):
#   print(x)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": "Park Lane 38" }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": { "$gt": "S" } }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": { "$regex": "^S" } }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# mydoc = mycol.find().sort("name")
# for x in mydoc:
#   print(x)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# mydoc = mycol.find().sort("name", -1)
# for x in mydoc:
#   print(x)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": "Mountain 21" }
# mycol.delete_one(myquery)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": {"$regex": "^S"} }
# x = mycol.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# mycol.drop()

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }
# mycol.update_one(myquery, newvalues)
# #print "customers" after the update:
# for x in mycol.find():
#   print(x)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# myresult = mycol.find().limit(5)
# for x in myresult:
#   print(x)

# x = requests.get('https://w3schools.com/python/demopage.htm')
# print(x.text)
