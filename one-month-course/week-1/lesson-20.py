print("Tip Calculator\n")

total_bill = float(input("What is your total bill?\n").replace("$", ""))

print("The total price of your account will be based on these three standard tip percentages: 15%, 18% or 20%\n")

bill_with_15_percent_tip = total_bill * (1 + 0.15)
bill_with_18_percent_tip = total_bill * (1 + 0.18)
bill_with_20_percent_tip = total_bill * (1 + 0.20)

print(f"Total bill with 15% tip: {bill_with_15_percent_tip:.2f}\n")
print(f"Total bill with 18% tip: {bill_with_18_percent_tip:.2f}\n")
print(f"Total bill with 20% tip: {bill_with_20_percent_tip:.2f}\n")

