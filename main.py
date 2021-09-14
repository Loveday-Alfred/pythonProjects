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
# weight = int(input('Weight '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} Kilos")
# else:
#     converted = weight // 0.45
#     print(f"You are {converted} Pounds")
#


# While loops
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print('Done')

# Guessing Game
# secretNumber = 9
# guessCount = 0
# guessLimit = 3
# while guessCount < guessLimit:
#     guess = int(input('Guess '))
#     guessCount += 1
#     if guess == secretNumber:
#         print('You won')
#         break
# else:
#     print('You lose')
#

# Car Game
# command = ""
# started = False
#
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("car is already started")
#         else:
#             started = True
#         print("car started...")
#     elif command == "stop":
#         if not started:
#             print("car is already stopped")
#         else:
#             started = False
#         print("car stopped...")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("sorry, i don't understand you")



# for loops

# for item in 'Python':
#     print(item)
#
# for items in range(5, 20, 2):
#     print(items)
# total = 0
# for itemss in [10, 20, 30]:
#      total += itemss
# print(f"Total : {total}")


# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")



number = [5, 2, 5, 2, 2]
for num in number:
    print("*" * num)


# List
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[4] = 'Marry'
print(names[2:4])
print(names)


large = [2, 4, 6, 8, 9, 10, 30, 50, 90, 49, 44]
for lg in large:
    print(lg)