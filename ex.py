import pandas as pd
import os

# Создание класса
class Payment:
    def __init__(self):
        pass

    # Создание метода для обработки и фильтра данных файла
    def processing1(self):
        try:
            with open('var5.svg', 'r') as file:
                print(file.read())
        except FileNotFoundError :
            print("Возникла следующая ошибка: [Errno2] No such file or directory")
    
    def processing2(self):
        try:
            with open('var5','r') as file:
                print(file.read())
        except FileNotFoundError:
            print('Возникла следующая ошибка:файл пуст')

    def processing3(self):
        try:
            with open('var5','r') as file:
                print(file.read())
                
        except:
            print('Возникла следующая ошибка:файл пуст')