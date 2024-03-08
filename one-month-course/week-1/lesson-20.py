print("Tip Calculator\n")

total_bill = input("What is your total bill?\n")

base_bill_amount = float(total_bill.replace("$", ""))

print("The total price of your account will be based on these three standard tip percentages: 15%, 18% or 20%\n")

bill_with_15_percent_tip = base_bill_amount * (1 + 0.15)
bill_with_18_percent_tip = base_bill_amount * (1 + 0.18)
bill_with_20_percent_tip = base_bill_amount * (1 + 0.20)

print(f"Total bill with 15% tip: {bill_with_15_percent_tip:.2f}\n")
print(f"Total bill with 18% tip: {bill_with_18_percent_tip:.2f}\n")
print(f"Total bill with 20% tip: {bill_with_20_percent_tip:.2f}\n")

