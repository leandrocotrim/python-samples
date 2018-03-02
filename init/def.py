def sum(a, b):
    return a + b
#print(sum(5, 6))

def double(a, b=2):
    return a * b
#print(double(2))
#print(double(5, b=4))

from datetime import date
d = (2017,6,26)
dt = date(*d)
#print(dt)

def new_user(active, admin):
    print(active)
    print(admin)

config = {'active':True, 'admin': False}
#new_user(**config)

def unpacking_arg(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)

#unpacking_arg(10,9,8,7,6,5,4,3,2,1,0)

def unpacking_kwargs(**kwargs):
    print(kwargs)
unpacking_kwargs(name='cotrim',age='30')







