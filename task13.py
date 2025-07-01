# 13. Ismlarni alfavit bo‘yicha tartiblang.
# Zafar Dilnoza Kamron Aziza Bekzod Alisher Anvar Bunyod

with open("Input/students.txt") as student:
    students = student.read().split()
    
    sortlangan_ismlar = sorted(students)
    
    
with open("Output/output13.txt","w") as javob:
    javob.write("sortlangan ismlar : " + ",".join(sortlangan_ismlar))

