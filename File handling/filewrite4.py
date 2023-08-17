x = [10, 20, 30, True, "Python"]

with open("iter.data","w") as fp:
    fp.writelines(str(x))
    print("Iterable data written")