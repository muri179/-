def f1(num):
    binary_list = []
    while True:
        remainder = num % 2
        binary_list.insert(0, str(remainder))
        num //= 2

        if num == 0:
            binary_string = ''.join(binary_list)
            print(f"Числото от десетична в двоична бройна система е: {binary_string}")

            answer = input("Желаете ли проверка 2->10 Y/N: ")
            if answer.upper() == 'Y':
                f2(binary_string)
            else:
                break

def f2(binary_string):
    decimal_number = int(binary_string, 2)
    print(f"Числото от двоична в десетична бройна система е: {decimal_number}")
num = int(input("Вашето число"))
if num > 0:
    f1(num)
else:
    print("Невалидно число")
