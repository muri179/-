list_vhod = []
def proizvedenie():
    result = 1
    for i in list_vhod:
        result *= int(i)
    list_vhod.clear()
    return result
a = ""
def Funct(a):
    result = proizvedenie()/ 2
    return print(result)
how_much = int(input("how much the program will work?:"))
for i in range(how_much):
    vhod = input("Danni").split(", ")
    for i in vhod:
        list_vhod.append(i)
    Funct(a)



