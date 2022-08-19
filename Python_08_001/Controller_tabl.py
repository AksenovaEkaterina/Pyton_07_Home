import Print_card
import logger_class
import join_tables

print(" 1 - Добавление данных об ученике\n 2 - Добавление данных об кабинете\n 3 - Вывод таблицы всех учеников\n 4 -  Вывод таблицы всех учеников\n 5 - Объединить таблицы данных" )

def button():
    cod_operation = int(input("введите код операции "))
    match cod_operation:
        case 1:
            logger_class.logger_student_card()
        case 2:
            logger_class.logger_classroom_card()
        case 3:
            Print_card.print_Student()
        case 4:
            Print_card.print_clas()
        case 5:
            join_tables.join_tables()
# button()