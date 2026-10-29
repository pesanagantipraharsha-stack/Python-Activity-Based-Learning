
n = int(input("Enter number of products: "))
total_replenishment = 0
total_discrepancy = 0

if n <= 0:
    print("Invalid number of products!")
else:
    for i in range(n):
        print("\nProduct", i + 1)

        name = input("Product name: ")
        opening = int(input("Opening stock: "))
        incoming = int(input("Incoming stock: "))
        dispatched = int(input("Dispatched stock: "))
        closing = int(input("Actual closing stock: "))
        minimum = int(input("Minimum required stock: "))
        if min(opening, incoming, dispatched,
               closing, minimum) < 0:
            print("Invalid stock quantity!")
            continue

        if dispatched > opening + incoming:
            print("Error: Insufficient stock!")
            continue

        expected = opening + incoming - dispatched
        discrepancy = closing - expected
        replenish = max(0, minimum - closing)

        print("\n--- Inventory Report ---")
        print("Product:", name)
        print("Expected Stock:", expected)
        print("Actual Stock:", closing)
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
    print("Inventory Reconciliation Completed")

