name = input("Employee Name: ")
basic = float(input("Basic Pay: "))
allowance = float(input("Allowances: "))
hours = float(input("Overtime Hours: "))
rate = float(input("Overtime Rate: "))
incentive = float(input("Incentives: "))
                  
if min(basic, allowance, hours, rate, incentive) < 0:
    print("Invalid input! Negative values not allowed.")

else:
    overtime = hours * rate
    gross = basic + allowance + overtime + incentive

    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 50000:
        deduction = 20000 * 0.05
        deduction += (gross - 20000) * 0.10
    else:
        deduction = 20000 * 0.05 + 30000 * 0.10
        deduction += (gross - 50000) * 0.15

    net = gross - deduction

    print("\n------ SALARY STATEMENT ------")
    print("Employee Name :", name)
    print(f"Basic Pay     : Rs.{basic:.2f}")
    print(f"Allowances    : Rs.{allowance:.2f}")
    print(f"Overtime Pay  : Rs.{overtime:.2f}")
    print(f"Incentives    : Rs.{incentive:.2f}")
    print("------------------------------")
    print(f"Gross Salary  : Rs.{gross:.2f}")
    print(f"Deductions    : Rs.{deduction:.2f}")
    print(f"Net Salary    : Rs.{net:.2f}")

