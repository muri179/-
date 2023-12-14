numbers = []
def multiply():
    result = 1
    for num in numbers:
        result *= int(num)
    print(result)
for x in input("Your numbers:").split(", "):
    numbers.append(x)
multiply()
