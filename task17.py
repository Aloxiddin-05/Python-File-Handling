#17. Ismi “A” harfi bilan boshlanuvchilarni alohida ro‘yxatga oling (`a_names.txt`).

with open("Input/students.txt") as student:
    students = student.read().split()
    
    
    hisob = []
    for i in students:
        if i[0].lower() == "a":
            hisob.append(i)
        
with open("Output/output17.txt","w") as javob:
    javob.write("A harfi bilan boshlanadigan ismlar:\n" + "\n".join(hisob))