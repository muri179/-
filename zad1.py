dict = {}
vhod = input("Вашите числа").split(", ")
for i in vhod:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
