#program to demonstrate file handling with w mode using "with open() as"

try:
    with open("stud.data","w") as st:
        print("File created and opend in w mode")
        print("is file closed:",st.closed)
        print("File name:",st.name)
        print("file mode:",st.mode)
        print("is file writable:",st.writable())
        print("is file readable:",st.readable())
        print("is file closed:",st.closed)
except FileNotFoundError:
    print("file does'nt exist")
finally:
    print("-------------------------------")
    print("I'am from finally block")
    print("is file closed:",st.closed)