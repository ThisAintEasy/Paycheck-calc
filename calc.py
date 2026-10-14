print ("Income and Savings Calc")
hourly = input("How much do you make per hour: ")
hour_ly = float(hourly)
debt = input("What do you pay for debt payments: ")
de_bt = int(debt)
debt_months = input("How many months do you want to save for: ")
payoff = int(debt_months)
bills = input("What do you pay in bills per month: ")
bill = int(bills)
savings = input("How much do you have saved: ")
save = int(savings)
hours = input("How many hours do you work a week: ")
hour = int(hours)

month = 0


inc_ome = hour_ly * hour
income = inc_ome * 4


step_one = income - bill
step_two = step_one - de_bt
step_three = step_two * payoff
step_four = step_three + save

print ("you will have", "$", step_four, "in", payoff, "months, if you stick to this budget.")
stay = input("Press enter to leave")
