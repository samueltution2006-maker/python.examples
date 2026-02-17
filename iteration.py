from collections import Counter

mylist = [ "1", "Hello", "3", "1" ]
mytuple = ("2", "World", 1000)
mydict = {  'A': 'One', 'B': 'Two' }
myset = { 'C', 'Three', 3, 'Four' }

for item in mylist:
    print(item)

listitr = iter(mylist)

for item in listitr:   #for item in mylist
    print(item);

tupleitr = iter(mytuple)

for item in tupleitr:
    print(item)

dictitr = iter(mydict)

for item in dictitr:
    print(item)

setitr = iter(myset)

for item in setitr:
    print(item)

print("List count=", Counter(mylist))
print("Tuple count=", Counter(mytuple))
print("Dic count=", Counter(mydict))
print("Set count=", Counter(myset))