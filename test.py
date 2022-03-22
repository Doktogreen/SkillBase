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