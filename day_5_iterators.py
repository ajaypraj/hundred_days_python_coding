# ====Iterator===> exmaple
# An iterator in python contains the countable number of elements that can be iterated upon.
# Iterator is object that allow you to traverse through all the elements and return one elemnt  at the one time
# basically it contains __iter__() and __next__() protocol

mytuple = ("apple", "banana", "Chikoo")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Every string is also iterable objects
s = "apple"
myit = iter(s)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# we can also use for loop for iterable objects
for x in mytuple:
    print(x)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            m = self.a
            self.a += 1
            return m
        else:
            raise StopIteration


x = MyNumbers()
myiter = iter(x)


for y in x:
    print(y)


# power calculation in python 2**1 to 2**10

class Power:
    def __iter__(self):
        self.power = 1
        return self

    def __next__(self):
        if self.power < 10:
            a = self.power
            self.power = self.power + 1
            return 2 ** a
        else:
            raise StopIteration


p = Power()
for x in p:
    print(x)
