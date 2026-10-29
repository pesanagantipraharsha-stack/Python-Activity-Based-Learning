name = input("Enter patient name: ")
print("1.General  2.Senior Citizen  3.Low Income")
category = int(input("Enter category (1-3): "))

consultation = float(input("Consultation charge: "))
diagnostic = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))

if (category not in (1, 2, 3) or
    min(consultation, diagnostic, treatment) < 0):
    print("Invalid input!")

else:
    total = consultation + diagnostic + treatment

    # Apply concession
    if category == 2:
        discount = 0.20
        patient_type = "Senior Citizen"
    elif category == 3:
        discount = 0.30
        patient_type = "Low Income"
    else:
        discount = 0
        patient_type = "General"

    concession = total * discount
    final_bill = total - concession

    if final_bill < 2000:
        classification = "Low Bill"
    elif final_bill <= 10000:
        classification = "Medium Bill"
    else:
        classification = "High Bill"

    print("\n--- Hospital Bill ---")
    print("Patient:", name)
    print("Category:", patient_type)
    print("Total: Rs.", round(total, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
    print("Classification:", classification)

