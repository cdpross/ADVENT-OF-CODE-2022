elf_calories_data = open(r'C:\Users\Courtney\OneDrive\Desktop\programming\ADVENT OF CODE 2022\DAY1\Elf_Calories.txt')
elf_calories = elf_calories_data.read().splitlines()

elf_sum = 0
one_elf = []
totals = []

for n in elf_calories:
    if n != "":
        one_elf.append(int(n))
    else:
        total = sum(one_elf)
        totals.append(total)
        one_elf = []
totals.sort()
print(max(totals))
top_three = totals[-3:]
print(sum(top_three))