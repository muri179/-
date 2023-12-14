y = 1
k=1

def f2(b):
    b = int(input("Вашето Число:"))
    if b != 0:
        k = f1(b)
        return print(k)
    else:
        print("Wrong Number")

def f1(x):
    if x == 0:
        f2(x)
    else:
        y = 4*x
        return print(y)

x = int(input("Вашето число:"))
f1(x)
