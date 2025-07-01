#10. Sonlar ro‘yxatini tartiblab, `sorted_numbers.txt` fayliga yozing.

with open("Input/numbers.txt") as number:
    numbers = number.read().split()
    numbers = list(map(int,numbers))
    
    sort_numbers = sorted(numbers)
    sort_numbers = list(map(str,sort_numbers))
    
with open("Output/output10.txt","w") as num:
    num.write("tartiblangan sonlar : "+"," .join(sort_numbers))