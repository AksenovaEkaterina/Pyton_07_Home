def сreate_student_card():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    birthday = input("Введите дату рождения: ")
    clas = input("Введите класс: ")
    student_card = f'{name} ,{surname} ,{birthday} ,{clas}'
    return student_card
    
# сreate_student_card()

def input_classroom ():
    lesson = input("Введите № урока: ")
    clas = input("Введите № кабинета: ")
    column = input("Введите № ряда: ")
    string = input("Введите № парты: ")
    variant = input("Введите № варианта: ")
    classroom_card=f'{lesson} ,{clas} ,{column} ,{string} ,{variant}'
    return classroom_card

# input_classroom ()