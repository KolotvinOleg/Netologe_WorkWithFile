import os


# Task_1
def from_file_to_dict(file_name: str) -> dict:
    cook_book = {}
    with open(file_name, encoding='utf-8') as f:
        lst = f.read().split('\n\n')
    for dish in lst:
        dish_lst = dish.split('\n')
        ingredients = []
        for i in range(2, int(dish_lst[1]) + 2):
            product = dish_lst[i].split(' | ')
            mini_dict = {'ingredient_name': product[0], 'quantity': product[1], 'measure': product[2]}
            ingredients.append(mini_dict)
        cook_book[dish_lst[0]] = ingredients
    return cook_book

# Task_2
def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            raise TypeError('Блюдо {dish} не содержится в кулинарной книге')
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': int(ingredient['quantity']) * person_count}
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    return shop_list


# Task_3
def get_result_file(path: str) -> None:
    files_lst = []
    for i in os.listdir(path):
        file_name = path + '\\' + i
        if os.path.isfile(file_name):
            with open(file_name, encoding='utf-8') as f:
                count_lines = len(f.readlines())
                files_lst.append([file_name, count_lines])
    files_lst = sorted(files_lst, key=lambda x: x[1])
    with open(path + '\\' + 'result.txt', 'a') as f:
        for file in files_lst:
            with open(file[0], encoding='utf-8') as l:
                file_text = l.read()
            f.write(file[0][file[0].rindex('\\') + 1:] + '\n')
            f.write(str(file[1]) + '\n')
            f.write(file_text)


# Test_Task_1
cook_book = from_file_to_dict('recipes.txt')
print(cook_book)

# Test_Task_2
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
print(get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 4))

# Test_Task_3
path = 'C:\\HomeWork_Python'
get_result_file(path)  # В результате должен быть создан файл result.txt
