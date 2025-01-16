import os
import time
import random

from colorama import Fore

from Companys import companyList
from GlobalVariables import money, stepCount, consumption, sharesConsumption


def nextStep(companyList,money, sharesConsumption):
    #Вероятности разных исходов и сами исходы


    #Вывод изначального списка
    os.system('cls' if os.name == 'nt' else 'clear')


    #Обновление списка с обновлением последней цены
    for act in companyList:
        act["last"] = act["price"]

    j = 0
    for act in companyList:

        probabilities = [1,4,20,50,20,4,1]

        events = ["Акции обвалились","Акции сильно упали","Акции умеренно упали",
            "Акции примерно сохранились",
            "Акции умеренно поднялись","Акции сильно поднялись","Акции стрельнули"
        ]

        status = random.choices(events, weights = probabilities, k = 1)[0]
        
        if status == "Акции обвалились":
            companyList[j]["price"] -= act["price"] - ((act["price"] / 100) * random.randint(50,81))
            companyList[j]["status"] = status

        elif status == "Акции сильно упали":
            companyList[j]["price"] -= act["price"] - ((act["price"] / 100) * random.randint(30,51))
            companyList[j]["status"] = status

        elif status == "Акции умеренно упали":
            companyList[j]["price"] -= act["price"] - ((act["price"] / 100) * random.randint(15,31))
            companyList[j]["status"] = status

        elif status == "Акции примерно сохранились":
            if random.randint(1,2) == 1:
                companyList[j]["price"] -= act["price"] - ((act["price"] / 100) * random.randint(0,16))
                companyList[j]["status"] = status
            else:
                companyList[j]["price"] += act["price"] + ((act["price"] / 100) * random.randint(0,16))
                companyList[j]["status"] = status

        elif status == "Акции умеренно поднялись":
            companyList[j]["price"] += act["price"] + ((act["price"] / 100) * random.randint(15,31))
            companyList[j]["status"] = status

        elif status == "Акции сильно поднялись":
            companyList[j]["price"] += act["price"] + ((act["price"] / 100) * random.randint(30,51))
            companyList[j]["status"] = status

        elif status == "Акции стрельнули":
            companyList[j]["price"] += act["price"] + ((act["price"] / 100) * random.randint(50,81))
            companyList[j]["status"] = status
        j += 1

    k = 0
    for i in companyList:
        companyList[k]["price"] = round(companyList[k]["price"],2)
        k += 1


    j = 0
    for i in companyList:
        if companyList[j]["price"] <= 10.00:
            companyList[j]["price"] = 10.00
        j += 1
        
    j = 0
    for i in companyList:
        if companyList[j]["price"] >= 70000.00:
            companyList[j]["price"] = 70000.00
        j += 1
        


    k = 0
    for i in companyList:
        print(Fore.WHITE + "Компания: " + companyList[k]["name"])


        if companyList[k]["price"] > companyList[k]["last"]:
            print("Цена акции: " + Fore.GREEN + str(companyList[k]["price"]))

        if companyList[k]["price"] < companyList[k]["last"]:
            print("Цена акции: " + Fore.RED + str(companyList[k]["price"]))

        if companyList[k]["price"] == companyList[k]["last"]:
            print(Fore.WHITE + "Цена акции: " + str(companyList[k]["price"]))


        print(Fore.WHITE + "Статус: " + companyList[k]["status"])
        k += 1
        print("")
    print("")
    print("Ежедневные траты: " + str(consumption))
    print("Налог за акции: " + str(sharesConsumption))
    print("")
    print(Fore.WHITE + "Введите любой символ для продолжения")
    input()


    #Вывод обновленного списка
    os.system('cls' if os.name == 'nt' else 'clear')

    return companyList, money, sharesConsumption
