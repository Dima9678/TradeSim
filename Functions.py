import os
import time

from Companys import companyList
from GlobalVariables import money, consumption, sharesConsumption




def start():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Добро пожаловать в симулятор трейдера")
    time.sleep(1)
    
    
    os.system('cls' if os.name == 'nt' else 'clear')






def checkList():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in companyList:
        print(f"{i['name']:<35}")
        print(f"Стоимость акции:{i['price']:>10.2f}")
        print("Акций у вас на руках: " + str(i["purchased"]))
        time.sleep(0.02)

    print("")
    print("0. Назад")

    while True:
        a = input()
        if a == "0":
            break
        else:
            print("Неправильный ввод, повторите еще раз")
            print("")
    os.system('cls' if os.name == 'nt' else 'clear')







def purchasedSharesCheck():

    os.system('cls' if os.name == 'nt' else 'clear')
    bought = False

    for i in companyList:
        if i['purchased'] > 0:
            bought = True
            print("Компания: " + i["name"])
            print("Акций на руках: " + str(i["purchased"]))
            print("")
            time.sleep(0.02)

    #Если у пользователя нет купленных акций
    if bought == False:
        print("У вас нет купленных акций")

    print("")
    print("0. Назад")

    while True:
        a = input()
        if a == "0":
            break
        else:
            print("Неправильный ввод, повторите еще раз")
            print("")

            
    os.system('cls' if os.name == 'nt' else 'clear')





def spending(money,sharesConsumption):
    #Траты каждого хода
    sharesConsumption = 0.0
    for i in companyList:
        if i["purchased"] > 0:
            sharesConsumption += ((i["price"] / 100) * i["purchased"])

    sharesConsumption = round(sharesConsumption, 2)
    money = money - consumption - sharesConsumption
    return money, sharesConsumption