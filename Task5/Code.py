plans = [
    ("Basic", 199, 2, 28, 50),
    ("Standard", 399, 5, 30, 40),
    ("Premium", 599, 10, 56, 30)
]

data = float(input("Required Data (GB): "))
days = int(input("Required Validity (days): "))
budget = float(input("Enter Budget: "))

best = None
minimum = float("inf")

if data < 0 or days <= 0 or budget < 0:
    print("Invalid input!")
else:
    print("\n--- Plan Comparison ---")

    for name, price, limit, validity, rate in plans:
        extra = max(0, data - limit)
        charge = extra * rate
        total = price + charge

        print("\nPlan:", name)
        print("Extra Charge: Rs.", round(charge, 2))
        print("Total Cost: Rs.", round(total, 2))

        if validity >= days and total <= budget:
            print("Status: Eligible")
            if total < minimum:
                minimum = total
                best = name
        else:
            print("Status: Not Eligible")

    print("\n--- Best Plan ---")
    if best:
        print("Recommended Plan:", best)
        print("Minimum Cost: Rs.", round(minimum, 2))
    else:
        print("No suitable plan found!")

