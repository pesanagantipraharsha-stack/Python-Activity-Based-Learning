

reports = []
n = int(input("Enter number of reports: "))

severity_points = {"high": 3, "medium": 2, "low": 1}

for i in range(n):
    print("\nReport", i + 1)
    name = input("Incident name: ")
    severity = input("Severity (High/Medium/Low): ").lower()
    location = input("Location: ").lower()
    frequency = int(input("Reported frequency: "))

    if severity not in severity_points or frequency < 1:
        print("Invalid report!")
        continue

  
    score = severity_points[severity]

    if location in ("lab", "hostel"):
        score += 2

    if frequency >= 3:
        score += 2


    if score >= 6:
        priority = "High"
    elif score >= 4:
        priority = "Medium"
    else:
        priority = "Low"

    reports.append((name, severity, location,
                    frequency, score, priority))
reports.sort(key=lambda x: (-x[4],
             -severity_points[x[1]], -x[3], x[2], x[0]))

print("\n----- PRIORITY SUMMARY -----")
for i, r in enumerate(reports, 1):
    print(i, r[0], "| Score:", r[4],
          "| Priority:", r[5])

print("\nTotal Reports:", len(reports))
print("High Priority:", sum(r[5] == "High" for r in reports))
print("Medium Priority:", sum(r[5] == "Medium" for r in reports))
print("Low Priority:", sum(r[5] == "Low" for r in reports))

