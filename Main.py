from colorama import Fore
import os
import time
import random

from Companys import companyList
from Functions import start, checkList, purchasedSharesCheck, sharesBuying, sharesSell
from GlobalVariables import money


start()


while True:
    print("Ваши деньги: " + str(round(money, 2)))
    print("")
    print("Выберите действие")

    print("1. Посмотреть список компаний")
    print("2. Посмотреть купленные акции")
    print("3. Купить акции")
    print("4. Продать акции")
    print("")
    print("5. Продолжить игру")
    print("")


    while True:   
        answer = input()
        if answer == "1":
            checkList()
            break
        elif answer == "2":
            purchasedSharesCheck()
            break
        elif answer == "3":
            money = sharesBuying(money)
            break
        elif answer == "4":
            money = sharesSell(money)
            break
        elif answer == "5":
            pass
            break
        else:
            print("Некорректный ввод, попробуйте заново")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')




