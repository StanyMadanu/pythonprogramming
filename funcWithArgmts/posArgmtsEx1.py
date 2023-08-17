def posarg(a, b, c, d, crs="Python"):  # function with formal parameters
    print("\t{}\t{}\t{}\t{}\t{}".format(a, b, c, d, crs))


# main program
print("-" * 50)
print("\tA\tB\tC\tD\tCourse")
print("-" * 50)
posarg(10, 20, 30, 40, )  # function call with pos arguments
posarg(d=40, c=30, a=10, b=20)  # function call with keyword arguments
posarg(10, 20, d=40, c=30)  # fun_call with pos arguments and keyword arguments
posarg(10, crs="Java", c=30, d=40, b=20)  # fun_call with pos, default and keyword arguments

print("-" * 50)
