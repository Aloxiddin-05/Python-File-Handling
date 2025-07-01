# 2. Fayldagi sonlar yig‘indisini hisoblang.

f = open("Input/numbers.txt", "r")
nums = f.read().split()

s = 0
for i in nums:
    s += int(i)

f1 = open("Output/output02.txt", "w")
f1.write(f"yig'indi:{s}")
