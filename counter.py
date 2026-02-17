from collections import Counter
import itertools

mystr = "Hello world"
mylst = [ ["One", 1, "Twwo", "One"], ["Three", "Four", 5, ("tuple1", "tuple2", "tuple3")] ]
mydct = { 'Key1': 5, 'Key2': 6 }
mytuple = ( 1, 2, 3, 2, 5 )

print("Mystr count", Counter(mystr))
print("Mylist count", Counter (itertools.chain(*mylst)) )
print("Mydct count", Counter(mydct.keys()) )
print("Mytuple count", Counter(mytuple))

_count = Counter()
#_count.update("Welcome to empty counter")
_count.update((1, 2, 3))


print("Empty counter", _count)

#for char in 'Hello':
#    print("%s %d", char, _count[char])

counter1 = Counter({ 'X': 1, 'Y': 2, 'Z': 3, 'A': 7 })
counter2 = Counter({ 'A': 5, 'B': 5, 'C': 6, 'Z': 4 })

counter3 = counter1 + counter2

print("Sum of two counters", counter3)

counter1.subtract(counter2)   # counter3 = counter1 - counter2
print("Substraction of counters", counter1)

#Counter1({ 'X': 1, 'Y': 2, 'Z': 3, 'A': -2 })
#Counter2({ 'A': 5, 'B': 5, 'C': 6, 'Z': 4})

print("Intersection ", counter1 & counter2)
print("Union", counter1 | counter2)


_elements = counter1.elements()

for element in _elements:
    print(element)