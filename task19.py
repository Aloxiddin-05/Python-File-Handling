#19. Barcha o‘quvchilar ismi va bahosini ekranga chiqaruvchi dastur yozing.

with open("Input/grades.csv") as name:
    names = name.read().splitlines()

natija = []
for i in names:
    if i.strip():
        name, grade = i.split(",")
        natija.append(f"Ism: {name}, Baho: {grade}")

with open("Output/output19.txt", "w") as javob:
    javob.write("\n".join(natija))

