import pandas as pd
import os




# Создание класса
class Payment:
    def __init__(self):
        pass

    # Создание метода для обработки и фильтра данных файла
    def processing(self):
        # Считывание основного файла
        df = pd.read_csv('var5.csv')
        try:
            with open('var5.svg', 'r') as file:
                print(file.read())
        except FileNotFoundError as Errno2:
            print("Возникла следующая ошибка: [Errno2] No such file or directory")
        except 
       