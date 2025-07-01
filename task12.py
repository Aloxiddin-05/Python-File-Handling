#12. Ismlar sonini hisoblang. 

with open("Input/students.txt") as student:
    students = student.read().split()
    
with open("Output/output12.txt","w") as chiqarish:
    chiqarish.write(f"ismlar soni: {len(students)}")
    