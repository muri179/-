def summarise():
    result = 0
    for i in list:
        result = sum(list)
        return(print(result))
def summarise_of_even():
    result = 0
    for i in list:
        if i % 2 == 0:
            result += i
    return(print(result))

list = []
numbers = input().split(", ")
for i in numbers:
    list.append(int(i))
summarise()
summarise_of_even()
