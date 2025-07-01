#11. Fayldagi barcha ismlarni ekranga chiqaring.

with open("Input/students.txt") as student:
    students = student.read()
    
with open("Output/output11.txt","w") as chiqarish:
    chiqarish.write(f"{students}")
    