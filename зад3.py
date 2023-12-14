import random
def count_it():
    list = []
    first_dict = {}
    final_dict = {}
    for i in range(1,10):
        list.append(random.randint(1,9))
    for i in list:
        if i in first_dict:
            first_dict[i] += 1
        else:
            first_dict[i] = 1
    sort_dict= sorted(first_dict.items(), key = lambda x: x[1] , reverse= True)
    top = sort_dict[:3]
    for element in top:
        final_dict[element[0]] = element[1]
    print(final_dict)
count_it()
