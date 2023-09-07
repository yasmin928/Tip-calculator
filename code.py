#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#print welcome statement
print("Welcome to tip calculator! ")

#input the bill amount and converting it into float
bill = float(input("What was the total bill? $ "))

#ask the user what percentage he like to give and coverting it into intergar
tip = int(input("What percentage tip you like to give? 10,12 or 15?  "))

#input how many peopel will split te bill
people = int(input("How many peopel to split the bill? "))

#calculate the percentage of the tip  and adding it to total bill
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill +total_tip_amount

bill_per_person = total_bill/people
#round to 2 decimal numbers
final_amount = round(bill_per_person ,2)

#print the final amount
print(f"Each  person should pay: ${final_amount}")
