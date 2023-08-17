# Program which will find all such numbers which are divisible by 4 but are not a multiple of 5, between 2456 and 3204 (both included).

for i in range(2456, 3204+1):
    if(i%4 == 0) and not(i % 5 == 0):
        print(i)