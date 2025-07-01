# 1. Fayldagi barcha sonlarni ekranga chiqaruvchi dastur yozing.

f = open("Input/numbers.txt", "r")

nums = f.readlines()
print(nums)

f2 = open("Output/output01.txt", "w")
f2.writelines(nums)
