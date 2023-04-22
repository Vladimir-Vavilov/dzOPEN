with open('reception.txt') as f:
    cockbook1 = f.read()
cockbook = {}
for cock in cockbook:
    key, value = cockbook.split(': ')
    cockbook.update({key: value})
print(cockbook1)
def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()
    for dish_name in dishes:
        if dish_name in cockbook:
            for ings in cockbook[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count
        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


