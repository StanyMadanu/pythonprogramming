Alph_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#left side triangle
for i in range(0,5):
    for j in range(i+1):
        print("*",end=" ")
    print()

#left side triangle numbers
for i in range(0,5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()

#left side triangle numbers
for i in range(0,5):
    for j in range(i+1):
        print(i+1,end=" ")
    print()

#left side triangle alphabets
for i in range(5):
    for j in range(i+1):
        print(Alph_list[j], end=" ")
    print()

#left side triangle alphabets
for i in range(5):
    for j in range(i+1):
        print(Alph_list[i], end=" ")
    print()


#left side triangle reverse
print("---left triangle reverse--------")
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()

for i in range(5):
    for j in range(5-i):
        print(j+1, end=" ")
    print()

for i in range(5):
    for j in range(5-i):
        print(5-i,end=" ")
    print()

for i in range(5):
    for j in range(5-i):
        print(Alph_list[j],end=" ")
    print()

for i in range(5):
    for j in range(5-i):
        print(Alph_list[i],end=" ")
    print()

#equal triangle with *
for i in range(5):
    for j in range(5-i-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end=" ")
    print()

#equal triangle with num's
for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(j+1, end=" ")
    print()

#equal triangle with num's
for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(i+1,end=" ")
    print()

#equal triangle with num's with Alphabets
for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(Alph_list[i],end=" ")
    print()

#equal triangle with num's with Alphabets
for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(Alph_list[j],end=" ")
    print()

#straight triangle reverse
print("---straight triangle reverse--------")
for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

#right angled triangle with *
for i in range(1,6):
    for j in range(1,6):
        if(j <= 5-i):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

#right angled triangle with num's
for i in range(1,5+1):
    for j in range(1,5+1):
        if(j <= 5-i):
            print(" ",end=" ")
        else:
            print(i,end=" ")
    print()

#right angled triangle with num's
for i in range(1,6):
    for j in range(5-i):
        print(" ", end=" ")
    for j in range((i-1)+1):
        print(j+1, end=" ")
    print()

#right angled triangle with alphabet's
for i in range(5):
    for j in range(5-i-1):
        print(" ", end=" ")
    for j in range(i+1):
        print(Alph_list[j],end=" ")
    print()

#right angled triangle with alphabet's
for i in range(5):
    for j in range(5-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(Alph_list[i],end=" ")
    print()

