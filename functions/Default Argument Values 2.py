def f(a, L = []):  # L will be shared
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

print('-----------------')


def f2(a, L=None): # fix the share problem
    if L is None:
        L = []
    L.append(a)
    return L


print(f2(1))
print(f2(2))
print(f2(3))
