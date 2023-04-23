# Special methods are methods with double underscore ex .__init__()--> for initslaization of objects
"""
1. They define how object of a class behave in certain situation such as how they are created,
compared and aritmetic operations.

Some common special methods are
--> __init__ called when instance of object is created
--> __str__  represents string representation of object and is called when is converted into string
--> __repr__ This method represents string representation of object and is called when object is printed
            and passed to repr() function
--> __len__ --> This method returns length of object and is called when len() function is used on object
--> __getitem__--> This method is used to get an item from object using [] notation
--> __setitem__ --> This method is used to set an item from object using [] notation
--> __delitem__  --> This method is used to delete an item from an object
-->__add__ --> This method is used to define the behaviour of the + operator when used with object of the
 class
 2. Operator overloading : Special methods can be used to operUsing ator overloading such as +, -, * , /, ==, !=,
 <, <=, >, >=
 3. __str__() and __repr__() -->called when converting object to string or passing to repr() method
 4. Object initializing : __init__
 5. attribute access control ==> __getattr__, __setattr__, __delattr__
 6. Object comparison ==> special methods are __eq__, __ne__, __gt__, __ge__
 7. Iteration : __iter__ and __next__ used to define custom iteration behaviour for instance of class
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "I am called when object instance is converted to str"

    def __repr__(self):
        print("Repr implementation")
        return "REPR is called"


p1 = Person("Ajay", 20)
print(p1.name, p1.age)
print(p1)  # print the object , then __str__ will be triggered
x = str(p1)  # converting obj to str will result in calling __str__
print(x)

print(repr(p1))
"""Repr implementation
REPR is called"""


class GFG:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return GFG(self.val + other.val)


obj1 = GFG(10)
obj2 = GFG(20)
print(obj1 + obj2)
m = obj1 + obj2
print(m.val)  # 30
