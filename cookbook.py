
with open ('recipes.txt', 'r', encoding='utf8') as file:
    dict = {}
    for line in file:
        dish_name = line.strip()
        dict[dish_name] = []
        for i in range(int(file.readline())):
            recept = file.readline().split(' | ')
            dict[dish_name].append({'ingredient_name':recept[0], 'quantity':int(recept[1]), 'measure':recept[2].strip()})
        file.readline()
print(dict)


