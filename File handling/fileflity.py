with open("addr2.data","a+") as fp:
    print("Name of the file:",fp.name)
    print("File mode:",fp.mode)
    print("is File Readable?=",fp.readable())
    print("is File Writable?=",fp.writable())
    print("is file closed=",fp.closed)


