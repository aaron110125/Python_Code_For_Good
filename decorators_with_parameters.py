# easy testing mechanism

#python decorators with parameters in Python (Multi-level Decorators)

def stringdecorator(dataType,msg1,msg2):
    def decorator(fun):
        print(msg1)
        def wrapper(*args, **kwargs):
            print(msg2)
            if all([type(arg) == dataType for arg in args]):
                return fun(*args, **kwargs)
            return "invalid input"
        return wrapper
    return decorator


@stringdecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
    st = ''
    for i in args:
        st += i
    return st

@stringdecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(stringJoin("It ", 'is ', "Decorators", 'Coding', "python"))
print()
print(summation(19,20,1,6,7,17,4,2,16))
