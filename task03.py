# 3. Fayldagi eng katta sonni aniqlang.

f1 = open("Input/numbers.txt", "r")
numbers = f1.read().split()

max_number = numbers[0]

for i in numbers:
    if int(i) > int(max_number):
        max_number = i

f = open("Output/output03.txt", "w")
f.write(f"max number = {max_number}")
