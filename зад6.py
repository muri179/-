from datetime import datetime
products = {}
total_amount = 0
while True:
    product_code = input("Въведете код на стока (00 за край на въвеждането): ")
    if product_code == '00':
        break
    price = float(input("Въведете цена на стока: "))
    quantity = int(input("Въведете брой стоки: "))
    products[product_code] = {'price': price, 'quantity': quantity}
    total_amount += price * quantity
print("\nКАСОВА БЕЛЕЖКА:")
for code, info in products.items():
    print("Код на продукта |", "Количество |", "Цена")
    print(f"{code}|{info['quantity']}|{info['price'] * info['quantity']:.2f} .")
print(f"\nОБЩА СУМА: {total_amount:.2f} лева.) {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
print(f"Дата и час:{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
paid_amount = float(input("Въведете предоставената сума пари: "))
change = paid_amount - total_amount
if change >= 0:
    print(f"Ресто: {change:.2f} лв.")
else:
    print(f"Сумата не е достатъчна!\nНе достигат {abs(change):.2f} лв.")
