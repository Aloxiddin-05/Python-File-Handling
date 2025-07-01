#15. `students.txt` faylidagi har bir ism nechta harfdan iboratligini ko‘rsating.

with open("Input/students.txt") as student:
    students = student.read().split()
    
    hisob = []
    for i in students:
        hisob.append(f"{i}: {len(i)} harfli")
        
with open("Output/output15.txt","w") as javob:
    javob.write("ismlar harflar soni:\n" + "\n".join(hisob))
    

    