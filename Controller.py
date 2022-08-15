from gettext import find
from http.client import OK
import logger
import logger



def print_all_cont ():
    with open ('Phone_book.txt', 'r', encoding='utf-8') as file:
        all_cont = file.read()
        print (all_cont)
        return (all_cont)

# print_all_cont ()

def create_new_cont ():
    logger.add_contact_tel_book()
    print ("Новый контакт создан")
# create_new_cont ()

def find_contact ():
    with open ('Phone_book.txt', 'r', encoding='utf-8') as file:
        all_cont = file.read()
        find_name = str(input("Введите имя абонента для поиска: "))
        find_cont = "Имя: "
        for i in range(len(all_cont)-len(find_name)):
            if(all_cont[i:i+len(find_name)]== find_name):
                while(all_cont[i]!="}"):
                    find_cont+=all_cont[i]
                    i+=1  
        return (find_cont)
# find_contact ()

def del_contact():
    with open ('Phone_book.txt', 'r', encoding='utf-8') as file:
        all_cont = file.read()
        del_name = str(input("Введите имя абонента для удаления: "))
        res = "}"
        start = 0
        finish = 0
        result = ""
        for i in range(len(all_cont)-len(del_name)):
            if(all_cont[i:i+len(del_name)]== del_name):
                start = i
                while (all_cont[i]!=res):
                 finish = i
                 i+=1
        for i in range(0, start-10): result+=all_cont[i]
        for i in range(finish+2, len(all_cont)):result+=all_cont[i]
    with open ('Phone_book.txt', 'w', encoding='utf-8') as file:
        file.write(result)
    print ("Контакт удален")
# del_contact()
print("Введите код операции:\n 1 - вывод информации о контакте в одной строке \n 1 - вывод информации о контакте в столбик \n 3 - поиск контакта по имени \n 4 - добавление контакта \n 5- удаление контакта ")
cod_operation = int(input('--> '))
if cod_operation ==1: print_all_cont ()
if cod_operation ==3: print (find_contact ())
if cod_operation ==4: print (create_new_cont ())
if cod_operation ==5: print (del_contact ())