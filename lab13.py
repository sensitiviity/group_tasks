import csv
import json

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

#необіхдно переписати дані з .json файла у .csv файл, при цьому додавши у файл кілька нових рядків