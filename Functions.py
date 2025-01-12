import os
import time

from Companys import companyList
from GlobalVariables import money

def start():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Добро пожаловать в симулятор трейдера")
    time.sleep(0.5)
    
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





def purchasedSharesCheck():

    os.system('cls' if os.name == 'nt' else 'clear')
    bought = False

    for i in companyList:
        if i['purchased'] > 0:
            bought = True
            print(f"{i['name']:<35}Количество акций:{i['purchased']:>10.2f}")
            time.sleep(0.02)

    #Если у пользователя нет купленных акций
    if bought == False:
        print("У вас нет купленных акций")

    print("")
    print("0. Назад")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')





def sharesBuying():
    global money

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Список акций:")
    j = 1
    for i in companyList:
        print(f"{j}. {i['name']:<35}Стоимость акции:{i['price']:>10.2f}")
        j += 1
        time.sleep(0.01)
    print("")
    print("Введите номер акции для покупки или 0 для отмены")

    isEnd = False
    answer = input()
    answer = int(answer)
    

    if answer != 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Компания: " + companyList[answer - 1]["name"])
        print("Стоимость одной акции: " + str(companyList[answer - 1]["price"]))
        print("Акций у вас на руках: " + str(companyList[answer - 1]["purchased"]))
        print("")
        print("Ваш баланс: " + str(money))
        print("")
        print("Введите количество акций, которое хотите купить или *отмена* для отмены покупки")
        print("")

        buyAnswer = input()
        

        if buyAnswer == "отмена":
            isEnd = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            buyAnswer = int(buyAnswer)
            print("Подтвердите покупку " + str(buyAnswer) + " акций на сумму " + str(buyAnswer * companyList[answer - 1]["price"]))
            print("*да* для подтверждения, *нет* для отмены")

            confirmationAnswer = input() 
            if confirmationAnswer == "нет":
                isEnd = True
                os.system('cls' if os.name == 'nt' else 'clear')
            elif confirmationAnswer == "да":
                if money >= buyAnswer * companyList[answer - 1]["price"]:
                    companyList[answer - 1]["purchased"] += buyAnswer
                    money -= buyAnswer * companyList[answer - 1]["price"]
            else:
                print("Некорректный ввод")
                time.sleep(1)
                isEnd = True
                os.system('cls' if os.name == 'nt' else 'clear')













    else:
        isEnd = True
        os.system('cls' if os.name == 'nt' else 'clear')


    if isEnd == False:
        print("0. Назад")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

sharesBuying()
    