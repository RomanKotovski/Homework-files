cookbook = []
with open ('recipes.txt', 'r', encoding='utf8') as cookbook_list:
    for line in cookbook_list:
        dish_name = line.strip()
        cook = {"Название блюда": dish_name, "Рецепт": []}
        ingredient_quantity = cookbook_list.readline()
        for i in range(int(ingredient_quantity)):
            quantity = cookbook_list.readline()
            ingredient_name, quantity, measure = quantity.split(' | ')
            ingredients_name = {'Название ингредиента':ingredient_name, 'количество': quantity, 'Единица измерения': measure.strip()}
            cook["Рецепт"].append(ingredients_name)
        cookbook_list.readline()
        cookbook.append(cook)
print(cookbook)