from colorama import Fore
import os
import time
import random

from Companys import companyList
from Functions import start, checkList, purchasedSharesCheck
from BuyFunc import sharesBuying
from SellFunc import sharesSell
from GlobalVariables import money, stepCount
from StepFunc import nextStep


start()


while True:
    print("Ход: " + str(stepCount))
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


    
    answer = input()

    if answer == "1":
        checkList()
    elif answer == "2":
        purchasedSharesCheck()
    elif answer == "3":
        money = sharesBuying(money)
    elif answer == "4":
        money = sharesSell(money)
    elif answer == "5":
        stepCount += 1
        companyList = nextStep(companyList)
        
        
    else:
        print("Некорректный ввод, попробуйте заново")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')