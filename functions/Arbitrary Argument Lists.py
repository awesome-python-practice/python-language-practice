def concat(a, *args, sep="/"):
    return a + sep.join(args)

print(concat("xx","a","b","c"))

