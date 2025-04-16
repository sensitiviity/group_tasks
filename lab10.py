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

