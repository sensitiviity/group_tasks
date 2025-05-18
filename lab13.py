import csv
import json

# Охріменко Валерія

#імена файлів
csv_file = "students.csv"
json_file = "students.json"

#дані для запису у csv
students_data = [
    ["Прізвище", "Ім'я", "Курс", "Група"],
    ["Шевченко", "Олена", 2, "КН-31"],
    ["Завгородній", "Олександр", 3, "КН-21"],
    ["Бондарчук", "Кирило", 1, "КН-41"]
]

#створення csv файлу та запис до нього даних
try:
    with open(csv_file, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students_data)
    print(f"CSV-файл успішно створено.")
except Exception as e:
    print("Помилка при записі у CSV-файл:", e)

#зчитування csv і запис у json
try:
    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students_list = list(reader)

    with open(json_file, mode="w", encoding="utf-8") as f_json:
        json.dump(students_list, f_json, ensure_ascii=False, indent=4)
    print(f"Дані з CSV успішно конвертовано у JSON-файл.")
except Exception as e:
    print("Помилка при конвертації з CSV у JSON: ", e)

# необхідно переписати дані з .json файла у .csv файл, при цьому додавши у файл кілька нових рядків


# Вакуленко Олександра

# Нові дані для додавання
new_students = [
    {"Прізвище": "Коваленко", "Ім'я": "Марія", "Курс": 2, "Група": "КН-32"},
    {"Прізвище": "Сидоренко", "Ім'я": "Андрій", "Курс": 3, "Група": "КН-22"}
]

try:
    # 1. Читаємо дані з JSON файлу
    with open(json_file, mode="r", encoding="utf-8") as f_json:
        students_data = json.load(f_json)
    
    # 2. Додаємо нових студентів
    students_data.extend(new_students)
    
    # 3. Записуємо оновлені дані назад у JSON
    with open(json_file, mode="w", encoding="utf-8") as f_json:
        json.dump(students_data, f_json, ensure_ascii=False, indent=4)
    print("Дані у JSON-файлі успішно оновлено.")
    
    # 4. Конвертуємо оновлений JSON у CSV
    with open(csv_file, mode="w", encoding="utf-8", newline="") as f_csv:
        # Отримуємо заголовки з першого запису
        fieldnames = students_data[0].keys()
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(students_data)
    print("Дані успішно конвертовано з JSON у CSV.")
    
    # Виводимо вміст файлів для перевірки
    print("\nВміст CSV файлу:")
    with open(csv_file, mode="r", encoding="utf-8") as f:
        print(f.read())
        
    print("\nВміст JSON файлу:")
    with open(json_file, mode="r", encoding="utf-8") as f:
        print(f.read())

except FileNotFoundError:
    print("Помилка: один з файлів не знайдено.")
except json.JSONDecodeError:
    print("Помилка: файл JSON містить некоректні дані.")
except PermissionError:
    print("Помилка: немає дозволу на запис у файл.")
except Exception as e:
    print(f"Невідома помилка: {e}")

# Завдання для наступного:
# 1. Додайте ще 2 нових студентів до JSON файлу
# 2. Реалізуйте перевірку на існування файлів перед читанням
# 3. Додайте функцію для виведення статистики (кількість студентів за курсами)

#Конопля Вікторія
# 1. Перевірка існування JSON перед читанням
import os
if os.path.exists(json_file):
    try:
        with open(json_file, mode="r", encoding="utf-8") as f:
            students_data = json.load(f)

        # 2. Додаємо ще двох студентів
        more_students = [
            {"Прізвище": "Мельник", "Ім'я": "Ігор", "Курс": 1, "Група": "КН-42"},
            {"Прізвище": "Тарасенко", "Ім'я": "Юлія", "Курс": 2, "Група": "КН-31"}
        ]
        students_data.extend(more_students)

        # Запис назад у JSON
        with open(json_file, mode="w", encoding="utf-8") as f:
            json.dump(students_data, f, ensure_ascii=False, indent=4)

        print("Додано ще 2 студенти до JSON-файлу.")

        # 3. Функція: статистика за курсами
        def show_course_stats(data):
            stats = {}
            for student in data:
                try:
                    course = int(student["Курс"])  # гарантуємо, що це int
                    stats[course] = stats.get(course, 0) + 1
                except ValueError:
                    print(f"Помилка курсу у записі: {student}")
    
            print("\nСтатистика студентів за курсами:")
            for course in sorted(stats):
                count = stats[course]
                print(f"Курс {course}: {count} студент{'и' if count != 1 else ''}")
        # Виклик функції
        show_course_stats(students_data)

    except Exception as e:
        print("Помилка при обробці JSON:", e)
else:
    print("Файл students.json не знайдено. Спочатку запустіть попередній код.")
#наступний студент повинен реалізувати:
#Додати у програму можливість видалення студента за прізвищем
#Додати ще 2 нових студенти до файлу students.json


