import pandas as pd

def print_Student():
    data1 =pd.read_csv('student.csv')
    data1.index +=1
    print(data1)
    return data1
# print_Student()

def print_clas():
    data2 =pd.read_csv('class.csv')
    data2.index +=1
    print(data2)
    return data2
# print_clas()

