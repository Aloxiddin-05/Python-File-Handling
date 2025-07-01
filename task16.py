#Ismi 5 harfdan uzun bo‘lgan talabalarni chiqaring.


with open("Input/students.txt") as student:
    students = student.read().split()
    
    hisob = []
    for i in students:
        if len(i) > 5:
            hisob.append(f"{i}: {len(i)} harfli")
        
with open("Output/output16.txt","w") as javob:
    javob.write("ismlar harflar soni:\n" + "\n".join(hisob))