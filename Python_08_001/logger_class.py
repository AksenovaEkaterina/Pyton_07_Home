import Create_card 

def logger_student_card():
    student_card = Create_card.сreate_student_card()
    with open("student.csv", 'a', encoding='utf-8') as file:
        file.writelines(f'{student_card}  \n')
    print ("Добавлено")
# logger_student_card()

def logger_classroom_card():
    classroom_card = Create_card.input_classroom ()
    with open("class.csv", 'a', encoding='utf-8') as file:
        file.write(f'{classroom_card}  \n')
    print ("Добавлено")
# logger_classroom_card()


