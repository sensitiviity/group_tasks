file_name = "question_answer.txt"  #назва файлу

#прізвище та питання наступному студенту
last_name = "Охріменко Валерія"
question = "Що таке списки у Python і як їх створити?"

try:
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Студент: " + last_name + "\n") #додавання до файлу імені
        f.write("Питання: " + question + "\n") #додавання до файлу запитання
    print(f"Файл успішно створено.")
except Exception as e:
    print("Сталася помилка при записі у файл: ", e)

#додати до файлу відповідь на питання


# Вакуленко Олександра

file_name = "question_answer.txt" 

# Моя інформація
my_name = "Вакуленко Олександра"

# Відповідь на попереднє питання
answer = """
Списки в Python - це змінні послідовності об'єктів, які:
1. Створюються через квадратні дужки: [1, 2, 3]
2. Можуть містити різні типи даних
3. Підтримують методи: append(), remove(), sort() тощо.

Приклад створення:
numbers = [1, 2, 3]
names = ['Anna', 'Ivan']
mixed = [1, 'text', True]
"""

# Нове питання для наступного студента
new_question = "Як працюють словники (dictionaries) в Python і чим вони відрізняються від списків?"

try:
    # Відкриваємо файл для додавання інформації
    with open(file_name, "a", encoding="utf-8") as f:
        # Додаємо роздільник
        f.write("\n\n")  
        # Додаємо свої дані
        f.write(f"Студент: {my_name}\n")
        f.write("Відповідь:\n")
        f.write(answer + "\n")
        f.write(f"Нове питання: {new_question}\n")
    
    print(f"Дані від {my_name} успішно додані до файлу!")
    
    # Перевіряємо вміст файлу
    print("\nПоточний вміст файлу:")
    with open(file_name, "r", encoding="utf-8") as f:
        print(f.read())

except FileNotFoundError:
    print("Помилка: файл не знайдено. Спочатку повинен бути створений файл.")
except PermissionError:
    print("Помилка: немає дозволу на запис у файл.")
except Exception as e:
    print(f"Невідома помилка: {e}")
