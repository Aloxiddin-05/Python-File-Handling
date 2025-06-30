# 13. Ismlarni alfavit bo‘yicha tartiblang.
# Zafar Dilnoza Kamron Aziza Bekzod Alisher Anvar Bunyod

f1 = open("Input/students.txt", "r+")

names = f1.readlines()
names.sort()

f2 = open("Ouput/output13.txt", "w")
f2.writelines(names)
