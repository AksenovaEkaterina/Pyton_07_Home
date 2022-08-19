import Create_data as tel_cont

def add_contact_tel_book ():
    new_cont = tel_cont.create_new_contact()
    with open ('Phone_book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{new_cont}\n')
# add_contact_tel_book ()
# def del_contact_tel_book ():


