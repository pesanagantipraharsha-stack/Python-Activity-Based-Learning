budget = float(input("Enter budget: "))
n = int(input("Number of products: "))
items = []

for i in range(n):
    name = input("\nProduct name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    items.append([name, price, qty])

def calculate():
    total = sum(p * q for _, p, q in items)
    discount = total * 0.10 if total >= 2000 else 0
    return total, discount, total - discount

total, discount, bill = calculate()
print("\nOriginal Bill: Rs.", round(bill, 2))

if budget < 0 or any(p < 0 or q < 0 for _, p, q in items):
    print("Invalid input!")
else:
    while bill > budget:
        available = [x for x in items if x[2] > 0]
        if not available:
            break
        costly = max(available, key=lambda x: x[1])
        costly[2] -= 1
        print("Reduced 1 quantity of", costly[0])
        total, discount, bill = calculate()

    print("\n--- Final Shopping Basket ---")
    for name, price, qty in items:
        print(name, "- Quantity:", qty)

    print("Total: Rs.", round(total, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Final Bill: Rs.", round(bill, 2))
    print("Remaining Budget: Rs.", round(budget - bill, 2))

