def ask_ok(p, retries=4, reminder="do that again"):
    while True:
        ok = input(p)
        if ok in ('y', 'yes'):
            return True
        if ok in ('n', 'no'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid input!')
        print(reminder)


ask_ok('input y/n: ', 2, 'retry it!')

