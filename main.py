# conditionals

housePrice = 1000000
hasGoodCredit = False
if hasGoodCredit:
    downPayment = 0.1 * housePrice
else:
    downPayment = 0.2 * housePrice
print(f'down payment is ${downPayment}')

# Logical operators
minName = 'jon'
if len(minName) < 3:
    print('Name must be at least three char long')
elif len(minName) > 50:
    print('Name must be 50 char or less')
else:
    print('name looks good')


# weight conversion
weight = input('Enter ur weight in L or K')
L = weight * 2
K = weight * 3
print()