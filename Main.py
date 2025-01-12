from colorama import Fore
import os
import time
import random


from Companys import companyList
from Functions import start, checkList


start()



money = 2000
while True:
    print("Ваши деньги: " + str(money))
    print("")
    print("Выберите действие")

    print("1. Посмотреть список компаний")
    print("2. Посмотреть купленные акции")
    print("3. Купить акции")
    print("4. Продать акции")
    print("")
    print("5. Продолжить игру")


    answer = input()
    if answer == "1":
        checkList()
    elif answer == "2":
        pass
    elif answer == "3":
        pass
    elif answer == "4":
       pass
    elif answer == "5":
        pass
    else:
        print("Некорректный ввод")




