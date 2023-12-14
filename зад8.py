def triangle_area(a, b):
    S = (a*b)/2
    return print(S,"квадратни сантиметра")
def square_area(a):
    S = a * a
    return print(S,"квадратни сантиметра")
def rectangle_area(a, b):
    S = a*b
    return print(S,"квадратни сантиметра")
figure = input()
if figure == "triangle":
    a = float(input("Страна:"))
    b = float(input("Височина:"))
    triangle_area(a, b)
elif figure == "square":
    a = float(input("Страна на квадрата:"))
    square_area(a)
elif figure == "rectangle":
    a = float(input("Първа страна:"))
    b = float(input("Втора страна:"))
    rectangle_area(a, b)


