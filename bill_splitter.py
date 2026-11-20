
current_total = 0

num_of_friends = 4

voorgerecht = 35.90
dinner = 67.50
drank = 22.80
dessert = 15.70

current_total = current_total + voorgerecht + dinner + drank + dessert
tip = current_total * 0.25
total_bill = current_total + tip
bill_each = total_bill / num_of_friends
bill_incl_tip = round(bill_each,2)
print(f'Bedrag per vriend is : {bill_incl_tip}')