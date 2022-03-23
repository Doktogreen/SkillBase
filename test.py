'''
    String Methods
'''

string = 'I am the best string in the world.'

print(len(string))
if 'am' in string:
    print('Oh yes am')

if 'best' not in string:
    print('I am not a best')
else:
    print('O yes I am a best')


print(string.capitalize())
print(string.casefold())
print(string.center(50))
print(string.center(50, '-'))
print(string.count('e', 5, 10))
print(string.endswith('ld.'))

tab_string = 'We \t are \t on \t our \t rightful way.'
print(tab_string.expandtabs())
print(tab_string.expandtabs(2))
print(tab_string.expandtabs(4))
print(tab_string.expandtabs(6))
print(tab_string.expandtabs(10))
print(string.find('am'))
print(string.find('am', 6, 10))

txt = "We have {:^8} chickens."
txt2 = "We have {:>8} chickens."
txt3 = "We have {:<8} chickens."
print(txt.format(49))
print(txt2.format(49))
print(txt3.format(49))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Object Method class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " and I am {}".format(self.age))
    print("Hello my name is " + self.name + " and I am", self.age)

p1 = Person("John", 36)
p1.myfunc()

#  Self Parameter class
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Inheritance 

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

# Adding properties
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of ", self.graduationyear)

x = Student("Ayomide", "Ajibodu", 2016)
x.welcome()

#  Iterator & Iterable

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

#  Creating an Iterator

class MyIterators:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        x += 1
        return x

myiterate = MyIterators()
myiter = iter(myiterate)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#  DateTime

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#  Regex 
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# SPLIT
x = re.split("\s", txt, 1)
print(x)

# REPLACE
x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)
print(x)

#  Try except, else, finally

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
