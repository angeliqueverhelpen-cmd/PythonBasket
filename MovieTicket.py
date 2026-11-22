
base_price = 12
seat_type = 'Gold'
age = 21
show_time = 'Evening'

is_member = False
is_weekend = False
discount = 0


if is_member and age >= 21:
    discount =3
print(f'Your discount is {discount:.2f}')

extra_charges = 0
if show_time == 'Evening' or is_weekend:
    extra_charges = 2
else:
    (print('No extra charges applied'))

print(f'Extra charges: {extra_charges:.2f}')


if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print(' You can book a ticket.')
    service_charges = 0
    if seat_type == 'Gold':
        service_charges = 5
    elif seat_type == 'Silver':
        service_charges = 3
    else:
        service_charges = 1
        print(f'Service charges: {service_charges:.2f}')

    final_price = base_price + extra_charges + service_charges - discount
    print(f'Your final ticketprice: {final_price:.2f}')
else:
    print(' You can not book a ticket.')









