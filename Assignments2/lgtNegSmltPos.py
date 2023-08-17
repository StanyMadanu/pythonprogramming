# Python program to find the largest negative and smallest positive numbers

lst = [10, 20, 30, -3, -5, -2]

def lrgNeg_smlPos(lst): #--------- Defining Function

    print("-"*50)
    print("\tGiven list: {}".format(lst))
    print("-"*50)

    #separating postive and negative numbers from given list
    pos_lst = [i for i in lst if i > 0] #------postive list
    neg_lst = [i for i in lst if i < 0] #------negative list
    
    large_neg = max(neg_lst) #---------storing max value from -ve list
    small_pos = min(pos_lst) #---------storing min value from +ve list

    print("\tThe Largest Negative value is = {}".format(large_neg))
    print("\tThe Smallest Positive Value is = {}".format(small_pos))
    print("-"*50)



lrgNeg_smlPos(lst) #------Function call