def f(ham: str, eggs: str = 'eggs') -> str:
    print("annotations:", f.__annotations__)
    print("args:", ham, eggs)
    return ham + " and " + eggs


print(f('hello'))
