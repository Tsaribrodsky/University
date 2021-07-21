# Modify the previous program such that only multiples of three or five
# are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

sum = 0
n = int(input("Please, enter a number: "))

for i in range(1, n+1):
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i

print(sum)