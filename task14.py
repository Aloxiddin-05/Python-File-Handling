#14. Ismlarni teskari tartibda chiqaring.

with open("Input/students.txt") as student:
    students = student.read().split()
    students.reverse()
    
    
with open("Output/output14.txt","w") as javobi:
    javobi.write("teskari tartiblangan ism :\n" + "\n".join(students))