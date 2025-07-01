#7. Fayldagi har bir sonni kvadratga ko‘paytirib ekranga chiqaring.

with open("Input/numbers.txt") as number:
    numbers = number.read().split()

    kvadrat = map(lambda x:str(pow(int(x),2)),numbers)
    
with open("Output/output07.txt","w") as num:
    num.write("barcha sonlar kvadratlari: " + " ".join(kvadrat))
