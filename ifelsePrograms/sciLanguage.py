# a program to find the scientist name as per their programming language - by using if else

print("C, Python, Java, C++")
lang = input("Enter any language as mentioned above: ")

if(lang=="C" or lang=="c"):
    print("{} language developed by Dennis Ritche".format(lang))
else:
    if(lang=="Python" or lang=="python" or lang=="PYTHON"):
        print("{} language developed by Guido Rossum".format(lang))
    else:
        if(lang=="Java" or lang=="java" or lang=="JAVA"):
            print("{} language developed by James Gosling".format(lang))
        else:
            if(lang=="C++" or lang=="c++"):
                print("{} language developed by Stroustrup".format(lang))
            else:
                print("Please enter languages as above mentioned only")