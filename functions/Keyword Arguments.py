def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot("xxyy")
parrot("xxyy", type="hello")
parrot("xxyy", state="john", type="function")


def cheeseShop(kind, *replies, **props):
    print('do u have any', kind, '?')
    for r in replies:
        print(r)
    print('-' * 40)
    for k in props:
        print(k, ':', props[k])


cheeseShop('cheeck', 'sorry, no', 'sorry, get off', a=1, b=2, c=3)
