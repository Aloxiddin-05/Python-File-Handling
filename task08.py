#8. Fayldagi sonlar ichidan 5 ga karralilarni sanang va ularni chiqaring.

with open("Input/numbers.txt") as number:
    numbers = number.read().split()
    numbers = list(map(int, numbers))
    
    karrali = filter(lambda x:x % 5 == 0,numbers)
    
with open("Output/output08.txt","w") as num:
    num.write("5ga karrali sonlar: " + " ".join(map(str,karrali)))