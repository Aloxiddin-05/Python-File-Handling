# 6. Fayldagi barcha toq sonlarni yangi `odd_numbers.txt` fayliga yozing.

with open("Input/numbers.txt") as num:
    numbers = num.read().split()
    toq = filter(lambda x: int(x) % 2 == 1, numbers)
    
with open("Output/output06.txt", "w") as number:
    number.write("toq sonlar: " + " ".join(toq))