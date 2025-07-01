# 5. Fayldagi sonlar o‘rtachasini (average) hisoblang.

with open("Input/numbers.txt") as num:
    numbers = num.read().split()
    sum = 0
    for i in numbers:
        i = int(i)
        sum += i
with open("Output/output05.txt", "w") as f:
    f.write(f"ortacha: {sum/len(numbers)}")
