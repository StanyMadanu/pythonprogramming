#Use global variable and perform nested functions with bitwise operators

a = 10 #global variable
b = 20 #global variable

def sample():
    print("\n=============Bitwise Operators====================")
    c = a << 2
    print("Bitwise Left shift Operator ({} << 2) = {}".format(a,c))

    def inside1():
        c1 = a >> 2
        print("Bitwise Right shift Operator ({} >> 2) ={}".format(a,c1) )

        def inside2():
            c2 = a | b
            print("Bitwise OR Operator ({} | {}) ={}".format(a,b,c2))

            def inside3():
                c3 = a & b
                print("Bitwise AND Operator ({} & {}) ={}".format(a,b,c3))

                def inside4():
                    c4 = ~ a
                    print("Bitwise Complement Operator (~{}) = {}".format(a,c4))

                    def inside5():
                        c5 = a ^ b
                        print("Bitwise XOR Operator ({} ^ {}) = {}".format(a,b,c5))

                    inside5() #calling inner function

                inside4() #calling inner function
            
            inside3() #calling inner function
        
        inside2() #calling inner function

    inside1() #calling inner function
    print("\n=============Bitwise Operators====================")

#main program
sample() #calling function
