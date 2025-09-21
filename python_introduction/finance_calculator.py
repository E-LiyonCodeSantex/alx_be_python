#values
monthly_income = int(input("Enter your monthly income: $"))
monthly_expenses = int(input("Enter your total monthly expenses: $"))

#Get user's daily savings
monthly_savings = monthly_income - monthly_expenses

#print user daily daving
print(f"Your monthly savings are ${monthly_savings}")

# Calculate user's yearly saving plus interest
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print user's yearly saving plus interest
print("Projected savings after one year, with interest, is: $", Projected_savings)
