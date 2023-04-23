class MyRange():
    def __init__(self,data):
        self.data=data
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        if self.index==len(self.data):
            raise StopIteration
        return self.data[self.index]


m=MyRange((1,2,3))
for n in m:
    print(n)
# https://gist.github.com/Zearin/2f40b7b9cfc51132851a

def new_decorator_funct(func):
    def wrapper():
        print("Before function execution we can add the code")
        func()
        print("After function execution added code")

    return wrapper


def standalone_func():
    print("I am standalone function. Do not dear to change me")


new_decorator_funct1 = new_decorator_funct(standalone_func)
new_decorator_funct1()

"""
Before function execution we can add the code
I am standalone function. Do not dear to change me
After function execution added code
"""


# Same thing can be implemented using below syntax

@new_decorator_funct
def another_standalone_func():
    print("I am standalone function. Do not dear to change me")


another_standalone_func()





    
    
