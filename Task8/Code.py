n = int(input("Enter number of locations: "))
total_replenishment = 0
total_discrepancy = 0

if n <= 0:
    print("Invalid number of locations!")

else:
    for i in range(n):
        print("\nLocation", i + 1)

        name = input("Location name: ")
        received = int(input("Stock received: "))
        distributed = int(input("Stock distributed: "))
        damaged = int(input("Stock damaged: "))
        actual = int(input("Actual remaining stock: "))
        minimum = int(input("Minimum required stock: "))

        if min(received, distributed, damaged,
               actual, minimum) < 0:
            print("Invalid stock quantity!")
            continue

        if distributed + damaged > received:
            print("Error: Stock usage exceeds received!")
            continue

        expected = received - distributed - damaged
        discrepancy = actual - expected
        replenish = max(0, minimum - actual)

        print("\n--- Stock Report ---")
        print("Location:", name)
        print("Expected Stock:", expected)
        print("Actual Stock:", actual)
        print("Discrepancy:", discrepancy)

        if discrepancy == 0:
            print("Status: Stock Matched")
        elif discrepancy < 0:
            print("Status: Stock Shortage")
        else:
            print("Status: Excess Stock")

        print("Replenishment Required:", replenish)

        total_replenishment += replenish
        total_discrepancy += abs(discrepancy)

    print("\n--- Final Summary ---")
    print("Total Replenishment:", total_replenishment)
    print("Total Absolute Discrepancy:", total_discrepancy)
    print("Stock Reconciliation Completed")
