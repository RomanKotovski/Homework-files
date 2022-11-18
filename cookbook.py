
def reading_book() -> dict:
    with open ('recipes.txt', 'r', encoding='utf8') as file:
        dict = {}
        for line in file:
            dish_name = line.strip()
            dict[dish_name] = []
            for i in range(int(file.readline())):
                recept = file.readline().split(' | ')
                dict[dish_name].append({'ingredient_name':recept[0], 'quantity':int(recept[1]), 'measure':recept[2].strip()})
            file.readline()
    return dict



def list_of_stores_with_ingredients(dishes: list, person_count: int, cook_book: dict) -> dict:
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],
                                                       'quantity': (consist['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return result



