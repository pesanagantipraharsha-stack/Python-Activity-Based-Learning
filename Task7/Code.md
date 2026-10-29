# 51. Bus Passenger Occupancy Simulation

## 1. Problem Statement

Write a Python program to simulate bus passenger occupancy across multiple stops. The program accepts boarding and alighting counts, calculates the number of passengers after each stop, and identifies capacity violations.

Conditions:

- Bus capacity is entered by the user.
- Passenger count cannot be negative.
- Alighting passengers cannot exceed the current occupancy.
- If occupancy exceeds capacity, display a warning.

## 2. Algorithm

1. Start the program.
2. Enter bus capacity and number of stops.
3. Initialize passenger count to zero.
4. Enter boarding and alighting counts at each stop.
5. Validate the passenger counts.
6. Update occupancy using:

Occupancy = Previous Occupancy − Alighting + Boarding

7. Check whether occupancy exceeds capacity.
8. Display occupancy and warnings.
9. Stop.

## 3. Flowchart 


``` mermaid

flowchart TD
A([Start]) --> B[Enter Capacity & Stops]
B --> C[Enter Boarding & Alighting]
C --> D[Calculate Occupancy]
D --> E{Capacity Exceeded?}
E -- Yes --> F[Display Warning]
E -- No --> G[Display Occupancy]
F --> G
G --> H{More Stops?}
H -- Yes --> C
H -- No --> I([Stop])
```


## 5. Sample Input


Enter bus capacity: 40
Enter number of stops: 4

Stop 1
Passengers boarding: 20
Passengers alighting: 0

Stop 2
Passengers boarding: 15
Passengers alighting: 5

Stop 3
Passengers boarding: 20
Passengers alighting: 5

Stop 4
Passengers boarding: 5
Passengers alighting: 15


## 6. Sample Output


Stop 1
Current Occupancy: 20
Status: Within capacity

Stop 2
Current Occupancy: 30
Status: Within capacity

Stop 3
Current Occupancy: 45
Warning: Capacity exceeded!

Stop 4
Current Occupancy: 35
Status: Within capacity

----- BUS SUMMARY -----
Final Occupancy: 35
Capacity Violations: 1
Simulation Completed


### Occupancy Calculation

| Stop | Boarding | Alighting | Occupancy | Status            |
| ---- | -------- | --------- | --------- | ----------------- |
| 1    | 20       | 0         | 20        | Normal            |
| 2    | 15       | 5         | 30        | Normal            |
| 3    | 20       | 5         | 45        | Capacity Exceeded |
| 4    | 5        | 15        | 35        | Normal            |

At Stop 3, the passenger count reaches 45, exceeding the bus capacity of 40 by 5 passengers.

