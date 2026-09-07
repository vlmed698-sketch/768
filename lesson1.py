student = {
    "Имя": "бУБЫЛДА",
    "Возраст": "18",
    "Группа": "1ИИ-2-11-26",
    "Город": "Novosibirsk",
    "Средний_балл": 4.7
}

print(student["Имя"])
print(student["Группа"])

def показать_студента(student):
    print(f"Имя: {student['Имя']}")
    print(f"Группа: {student['Группа']}")
    print(f"Город: {student['Город']}")

показать_студента(student)

import json
json_text = json.dumps(student, ensure_ascii=False, indent=2)
print(json_text)

def общая_информация(student):
     print(f"Имя: {student['Имя']}, Группа: {student['Группа']}, Город: {student['Город']}")
     
общая_информация(student)

if student["Средний_балл"] >= 4.0:
    print('Красаучек, высокий балл!')

if student["Город"] == "Moscow":
    print('Москвич что ли?')
else:
    print('Колхоз приехал')