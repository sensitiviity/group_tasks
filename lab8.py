#завдання: створити словник + реалізувати функцію додавання даних

#структура словника:
# номер групи,
# ПІБ студента,
# курс,
# предмети та оцінки за семестр

students = {
    "Іваненко Роман Андрійович": {
        "група": "КН-31",
        "курс": 2,
        "предмети": {
            "Чисельні методи": [90, 85],
            "Програмування мовою Python": [95, 92],
            "Сучасні парадигми програмування": [78, 85]
        }
    },
    "Шевченко Марія Олександрівна": {
        "група": "КН-31",
        "курс": 2,
        "предмети": {
            "Чисельні методи": [88, 84],
            "Програмування мовою Python": [91, 93],
            "Сучасні парадигми програмування": [95, 92]
        }
    }
}

#список предметів
subjects_list = [
    "Чисельні методи",
    "Програмування мовою Python",
    "Сучасні парадигми програмування"
]

#Охріменко Валерія

#вивід вмісту словника
def print_students():
    print("\nСписок студентів:")
    for name, info in students.items():
        print(f" - {name}:")
        print(f"Група: {info['група']}")
        print(f"Курс: {info['курс']}")
        for subject, marks in info['предмети'].items():
            print(f"{subject}: {marks}")

#додавання нового студента до словника
def add_student():
    full_name = input("Введіть ПІБ студента: ")
    group = input("Введіть номер групи: ")
    course = int(input("Введіть курс: "))

    #запит оцінок для кожного з предметів
    subjects = {}
    for subject in subjects_list:
        marks_input = input(f"Введіть оцінки з '{subject}' через кому: ")
        #перетворюємо введений рядок у список чисел
        marks = list(map(int, marks_input.split(',')))
        subjects[subject] = marks

    #додавання даних про студента до головного словника
    students[full_name] = {
        "група": group,
        "курс": course,
        "предмети": subjects
    }
    print(f"\nНовий студент успішно доданий.")

while True:
    print("\nМеню:")
    print("1. Показати усіх студентів")
    print("2. Додати нового студента")
    print("3. Вихід")

    choice = input("Ваш вибір (1-3): ")

    if choice == "1":
        print_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        print("Програму завершено.")
        break
    else:
        print("Оберіть дію із меню.")

# у програмі необхідно реалізувати:
# функцію для сортування студентів за середнім балом з предмета, який обере користувач

# також перевірити, чи структура словника є оптимальною, і за потреби змінити


# Вакуленко Олександра
# Оптимізація структури словника:
# 1) Додано середній бал до інформації про кожного студента
# 2) Додано функцію сортування за середнім балом з обраного предмета

def calculate_average_marks():
    """Розраховує середній бал для кожного студента"""
    for student in students.values():
        student['середній_бал'] = {}
        for subject, marks in student['предмети'].items():
            student['середній_бал'][subject] = sum(marks) / len(marks)

def sort_by_subject_average():
    """Сортує студентів за середнім балом з обраного предмета"""
    calculate_average_marks()  # Спочатку розраховуємо середні бали
    
    print("\nДоступні предмети:")
    for i, subject in enumerate(subjects_list, 1):
        print(f"{i}. {subject}")
    
    try:
        choice = int(input("Оберіть предмет для сортування (1-3): ")) - 1
        selected_subject = subjects_list[choice]
        
        # Створюємо список кортежів (середній бал, ПІБ студента)
        student_avg = [
            (info['середній_бал'][selected_subject], name)
            for name, info in students.items()
        ]
        
        # Сортуємо за середнім балом (в порядку спадання)
        student_avg.sort(reverse=True)
        
        print(f"\nСтуденти, відсортовані за середнім балом з '{selected_subject}':")
        for avg, name in student_avg:
            print(f"{name}: {avg:.1f}")
            
    except (ValueError, IndexError):
        print("Невірний вибір предмету.")

# Головне меню
while True:
    print("\nМеню:")
    print("1. Показати усіх студентів")
    print("2. Додати нового студента")
    print("3. Сортувати за середнім балом з предмету")
    print("4. Вихід")

    choice = input("Ваш вибір (1-4): ")

    if choice == "1":
        print_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        sort_by_subject_average()
    elif choice == "4":
        print("Програму завершено.")
        break
    else:
        print("Оберіть дію із меню.")

# Наступний може реалізувати:
# 1) Функцію пошуку студентів за діапазоном середнього балу
# 2) Функцію редагування даних про студента
# 3) Функцію видалення студента зі словника
