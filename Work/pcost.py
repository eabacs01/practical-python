# pcost.py
#
# Exercise 1.27

total_cost = 0
with open('Data\portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        _, numshares, price = tuple(line.split(','))
        total_cost += int(numshares) * float(price)
        
print(f'Total cost: {total_cost}')