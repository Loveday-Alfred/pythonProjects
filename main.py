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



# number = [5, 2, 5, 2, 2]
# for num in number:
#     print("*" * num)
#
#
# # List
# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[4] = 'Marry'
# print(names[2:4])
# print(names)
#
#
# large = [2, 4, 6, 8, 9, 10, 30, 50, 90, 49, 44]
# max = large[0]
# for lg in large:
#     if lg > max:
#         max = lg
# print(max)



# 2 dimensional List
# matrix = [
#     [2, 4, 5],
#     [4, 8, 7],
#     [7, 8, 7]
# ]
#
# # print(matrix[0][2])
# for row in matrix:
#     print(row)
#     for item in row:
#         print(item)
#
#
# List methods
# number = [2, 4, 5, 6, 8, 9, 20]
# number.insert(0:20)
# number.append(20)
# number.remove(5)
# number.pop()
# number.clear()
# number.sort()
# number.reverse()
# number2 = number.copy() gives another copy of the list




dup = [2, 2, 3, 3, 5, 6, 7, 8, 9, 8, 3]
unique = []
for dups in dup:
    if dups not in unique:
        unique.append(dups)
print(unique)




# Tuples
# tuples can't be modify, they r immutable
# numbers = (1, 4, 7)


# unpacking
# i find unpacking very similar to destructuring
coordinates = (1, 3, 6)
x, y, z = coordinates
print(x, y, z)





# Dictionaries in python
# we use dictionaries to store key pairs in python
# i find dictionaries similar to objects in JS
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "isVerified": True
# }
# print(customer["isVerified"])
# customer["birthdate"] = "Jan 1 1999"
# print(customer["birthdate"])





phone = input("Phone: ")
