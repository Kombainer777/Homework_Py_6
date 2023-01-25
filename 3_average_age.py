#3. Еще немного о друзьях
#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
#Создайте список friends и добавьте в него N словарей с ключами name и age.
#Выведите средний возраст всех друзей и самое длинное имя.

n = int(input("Введите количество друзей: "))
friends = []
new_friend = {}
for element in range(0, n):
    name = input("Введите имя друга: ")
    age = int(input("Введите возраст друга: "))
    new_friend["name"] = name
    new_friend["age"] = age
    friends.append(new_friend)
    new_friend = {}
print("Список Ваших друзей: ", friends)

aver_age = 0
longest_name = friends[0]['name']
for element in friends:
    aver_age = aver_age + element['age']
    if len(element['name']) > len(longest_name):
        longest_name = element['name']
aver_age = aver_age/n
print("Средний возраст Ваших друзей составляет:  ", round(aver_age, 1))
print()
print("Самое длинное имя: ", longest_name)