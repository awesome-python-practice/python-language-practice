def add(base):
    return lambda x: x + base


f = add(10)
print(f(1))
print(f(2))
print(f(3))
