# Assignment 2: Give me a tower of hanoi - 5 levels

# Expected OUTPUT PART 1:
#                   1
#               3       3
#           5       5      5 
#       

# Expected OUTPUT PART 2:

# Row 1 : 1s = 1
# Row 2 : 3s = 3 * 2 = 6
# Row 3 : 5s = 5 * 3 = 15

ran = int(input("Enter range: "))
distance = int(input("Enter distance: "))

p = 1
lst = []

for i in range(1, ran + 1):
    x = 0
    while x < ran - i:
        print(end = " ")
        x += 1
    for j in range(i):
        print(p, end=" ")
    lst.append(p * i)
    p += distance
    print()

print("\n", lst)