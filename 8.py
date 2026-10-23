print("Здравствуйте! Как Вас зовут?")
name = input()
print(f"Очень приятно, {name}! Меня зовут Марк.")
print("Сколько Вам лет?")
age = int(input())
markage = 78
if age < markage:
    conclusion = markage - age
    print(f"Да, {name}, я старше Вас на {conclusion} лет.")
elif markage < age:
    conclusion = age - markage
    print(f"Да, {name}, Вы старше меня на {conclusion} лет.")
else:
    print(f"Да, {name}, мы с Вами ровесники!")
print("Вам нравится программировать?")
answer = input().lower()
if answer == "да":
    print("Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.")
else:
    print("Жаль. Я думал, Вы сможете написать интересную программу для меня.")