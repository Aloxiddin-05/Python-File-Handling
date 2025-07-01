# 4. Fayldagi barcha juft sonlarni chiqaring.

with open("Input/numbers.txt") as num:

    numbers = num.read().split()


juft = filter(lambda x: int(x) % 2 == 0, numbers)

with open("Output/output04.txt", "w") as f:
    f.write("Juft sonlar: " + " ".join(juft))
