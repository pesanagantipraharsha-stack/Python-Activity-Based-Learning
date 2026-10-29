
capacity = int(input("Enter bus capacity: "))
stops = int(input("Enter number of stops: "))

passengers = 0
violations = 0

if capacity <= 0 or stops <= 0:
    print("Invalid capacity or stops!")

else:
    for i in range(1, stops + 1):
        print("\nStop", i)

        board = int(input("Passengers boarding: "))
        alight = int(input("Passengers alighting: "))
      
        if board < 0 or alight < 0:
            print("Invalid passenger count!")
            break

        if alight > passengers:
            print("Error: Alighting exceeds occupancy!")
            break
        passengers = passengers - alight + board

        print("Current Occupancy:", passengers)


        if passengers > capacity:
            print("Warning: Capacity exceeded!")
            violations += 1
        else:
            print("Status: Within capacity")

    print("\n----- BUS SUMMARY -----")
    print("Final Occupancy:", passengers)
    print("Capacity Violations:", violations)
    print("Simulation Completed")

