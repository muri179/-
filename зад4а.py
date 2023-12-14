list=[]
for x in input("Numbers:", ).split(", "):
    list.append(x)
def multiplyer():
    multy = 1
    for i in list:
        multy *= int(i)
    print(multy)

multiplyer()
