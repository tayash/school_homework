# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_student_name():
    my_class_lst = [{'Name': "Роман Бойко", 'Number': 1},
                   {'Name': "Юрій Бойко", 'Number': 2},
                   {'Name': "Соломія Викович", 'Number': 3},
                   {'Name': "Кирило Гарбуз", 'Number': 4},
                   {'Name': "Христина Гринюк", 'Number': 5},
                   {'Name': "Софія Губаль", 'Number': 6},
                   {'Name': "Богдан Гупало", 'Number': 7},
                   {'Name': "Таїсія Шевченко", 'Number': 8}]

    print("Введіть номер учня:")
    x = input()
    x = int(x)
    total_students = len(my_class_lst)
    if x > total_students:
        print(f"Номер завеликий, у класі лише {total_students} учнів.")
    else:
        for i in my_class_lst:
            student_num = i.get("Number")
            student_name = i.get("Name")
            if student_num == x:
                print(f"Ім'я учня з номером {x}: {student_name}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_student_name()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
