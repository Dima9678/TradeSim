import os
import time

from Companys import companyList

def start():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Добро пожаловать в симулятор трейдера")
    time.sleep(2)
    
    os.system('cls' if os.name == 'nt' else 'clear')


def checkList():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in companyList:
        print(f"{i['name']:<35}Стоимость акции:{i['price']:>10.2f}")
        time.sleep(0.02)

    print("")
    print("0. Назад")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')