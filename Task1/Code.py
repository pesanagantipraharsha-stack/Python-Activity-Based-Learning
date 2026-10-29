applicants = []
n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nApplicant", i + 1)
    name = input("Enter student name: ")
    marks = float(input("Enter aggregate marks (%): "))
    subjects = list(map(float, input(
        "Enter marks in 3 subjects: ").split()))
    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter annual family income: Rs. "))

    if (marks >= 75 and min(subjects) >= 60
            and attendance >= 75 and income <= 250000):
        applicants.append(
            (name, marks, attendance, income))
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")
      
applicants.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- Scholarship Merit List ---")

if applicants:
    for rank, student in enumerate(applicants, 1):
        print(f"{rank}. {student[0]} - Marks: {student[1]}%, "
              f"Attendance: {student[2]}%, Income: Rs.{student[3]}")
else:
    print("No eligible applicants")
