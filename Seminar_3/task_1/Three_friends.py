# Задание № 8.

# 1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
#   * Какие вещи взяли все три друга
#   * Какие вещи уникальны, есть только у одного друга
#   * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
#   * Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

dict_friends_with_things = {"Ivan":("food", "sleeping_bag", "first_aid_kit"), "Petr":("knife", "food", "fishing_rod"), "Oleg":("food", "fishing_rod", "knife")}

list_of_things = []

list_of_unique_items = []

for key, value in dict_friends_with_things.items():

    list_of_things += value    
    
print(f"\nСписок вещей, которые взяли друзья:\n{list_of_things}\n")


for item in list_of_things:

    count_elements = list_of_things.count(item)


    if count_elements > 1:
         
         for i in range(count_elements):
           



            list_of_things.remove(item)
      

print(f"\n{list_of_things}")
