def set_gen(spisak):
    result = set()
    for num in (spisak):
        number_of_matches = spisak.count(num)
        if number_of_matches == 1:
            result.add(num)
        else:
            result.add(num)
            for i in range(2, number_of_matches + 1):
                result.add(str(num)*i)
    return result

spisak = [1,1,2,3,4,5,5,5,5,6,6,7,8,9,9,]
print(set_gen(sorted(spisak)))
