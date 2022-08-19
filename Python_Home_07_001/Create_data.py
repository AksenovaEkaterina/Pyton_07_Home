
def create_new_contact():
    global contact
    global name
    name = input ("Введите имя ")
    surname = input ("Введите фамилию ")
    tel_number = input ("Введите номер телефона ")
    name_info = input ("Введите дополнительную информацию ")
    contact = \
        {
        "Имя": name,
        "Фамилия": surname,
        "Номер телефона": tel_number,
        "Дополнительная информация": name_info,
        }
    # print (contact)
    return (contact)
  
    
# create_new_contact()
  
