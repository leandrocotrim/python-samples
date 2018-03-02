def double(x):
    '''
    dobro
    '''
    return x * 2

def apply_to_one(f):
    '''
    Aplica o n 1 a função passada
    '''
    return f(1)

def sum(a=0, b=0):
    '''
    soma os valores
    '''
    return a + b

print(double(2))
d = double
print(apply_to_one(d))

l = lambda x: x + 4

print(apply_to_one(l))
print(sum())
print(sum(b=1))