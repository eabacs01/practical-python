# mortgage.py

def principal_paid(principal, payment):
    if payment > principal:
        return 0, principal
    else:
        return principal - payment, payment 

principal = 500000.0
rate = 0.05
payment = 2684.11
over_payment = 1000.0
over_payment_month_start = 5 * 12 + 1
over_payment_month_end = over_payment_month_start + 48 - 1
month = 1
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) 
    
    if month >=over_payment_month_start and month <= over_payment_month_end:
        principal, paid = principal_paid(principal, payment + over_payment)
    else:
        principal, paid = principal_paid(principal, payment)
    
    total_paid = total_paid + paid
    print(f'{month:10d} | {total_paid: 12.2f} | {principal: 12.2f}')
#    print(month, round(total_paid,2), round(principal,2))
    month = month + 1


print('Total paid', round(total_paid,2))
print('Months', month - 1)