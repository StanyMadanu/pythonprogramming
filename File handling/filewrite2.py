#writing the data from kbd

with open("addr2.data","w") as fp:
    print("Enter the data (press @ to finish):")
    while(True):
        kbdata = input()
        if(kbdata=="@"):
            break
        else:
            fp.write(kbdata + "\n")
    print("Data Written to the file successfully..!")