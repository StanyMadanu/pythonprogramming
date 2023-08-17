import shares
import importlib, time

def disshares(d):
    print("="*50)
    print("\tShare Name\tShare Value")
    print("="*50)
    for sn, sv in d.items():
        print("\t{}\t\t{}".format(sn,sv))
    print("="*50)


#main program
d = shares.sharesinfo()
disshares(d)
print("PVM goes to sleep for 10 seconds")
time.sleep(10)
print("PVM completed sleep for 10 seconds")
importlib.reload(shares)
d = shares.sharesinfo()
disshares(d)
time.sleep(10)
importlib.reload(shares)
d = shares.sharesinfo()
disshares(d)
