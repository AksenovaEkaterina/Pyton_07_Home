import Print_card

def join_tables():
    data1=Print_card.print_Student()
    data2=Print_card.print_clas()
    data3 = data1.join(data2)
    print(data3)
# join_tables()