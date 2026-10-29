# University Scholarship Allocation System using Python

## 1. Problem Statement

The University Scholarship Allocation System evaluates students based on aggregate marks, subject-wise minimum marks, attendance percentage, and family annual income. It identifies eligible students and ranks them according to aggregate marks. If two students have equal marks, attendance is used as the first tie-breaker, followed by lower family income. The system displays the final ranked list of eligible students.

## 2. Algorithm

1. Start the program.
2. Read the number of applicants.
3. Enter each student's name, aggregate marks, subject marks, attendance percentage, and annual family income.
4. Check the eligibility criteria:
   - Aggregate marks must be at least 75%.
   - Every subject mark must be at least 60%.
   - Attendance must be at least 75%.
   - Annual family income must not exceed ₹2,50,000.
5. Add eligible students to the eligible list.
6. Sort eligible students by:
   - Higher aggregate marks first.
   - Higher attendance first if aggregate marks are equal.
   - Lower family income first if both are equal.
7. Display the ranked list of eligible students.
8. If no students qualify, display a suitable message.
9. Stop the program.

## 3. Flowchart 
```mermaid
flowchart TD
    A([Start]) --> B[/Enter student details/]
    B --> C{Meet all criteria?}
    C -- No --> D[Not Eligible]
    C -- Yes --> E[Add to eligible list]
    D --> F{More students?}
    E --> F
    F -- Yes --> B
    F -- No --> G[Rank students]
    G --> H[Display results]
    H --> I([Stop])
```

## 5. Sample Input

Enter number of applicants: 3

Applicant 1
Enter student name: Ravi
Enter aggregate marks (%): 85
Enter marks in 3 subjects: 80 90 75
Enter attendance (%): 90
Enter annual family income: Rs. 200000

Applicant 2
Enter student name: Sita
Enter aggregate marks (%): 85
Enter marks in 3 subjects: 75 80 70
Enter attendance (%): 95
Enter annual family income: Rs. 220000

Applicant 3
Enter student name: Aman
Enter aggregate marks (%): 70
Enter marks in 3 subjects: 65 70 75
Enter attendance (%): 80
Enter annual family income: Rs. 150000


## 6. Sample Output

Applicant 1
Eligible for scholarship

Applicant 2
Eligible for scholarship

Applicant 3
Not eligible for scholarship

--- Scholarship Merit List ---
1. Sita - Marks: 85.0%, Attendance: 95.0%, Income: Rs.220000.0
2. Ravi - Marks: 85.0%, Attendance: 90.0%, Income: Rs.200000.0

