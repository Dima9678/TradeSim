import os
import time

from Companys import companyList
from GlobalVariables import money

def start():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Добро пожаловать в симулятор трейдера")
    time.sleep(1)
    
    
    os.system('cls' if os.name == 'nt' else 'clear')






def checkList():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in companyList:
        print(f"{i['name']:<35}Стоимость акции:{i['price']:>10.2f}")
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
            print(f"{i['name']:<35}Количество акций:{i['purchased']:>10.2f}")
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








def sharesBuying(money):

    

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Ваши деньги: " + str(round(money, 2)))
    print("")
    print("Список акций:")
    j = 1
    for i in companyList:
        print(f"{j}. {i['name']:<35}Стоимость акции:{i['price']:>10.2f}")
        j += 1
        time.sleep(0.01)
    print("")
    
 
    isEnd = False
    flag = False
    flag2 = False

    while True:
        if flag == True:
            break
        if flag2 == True:
            break
        
        print("Введите номер акции для покупки или 0 для отмены")
        
        #Номер акции, которую хотим купить
        answer = input()

        if answer == "0":
            isEnd = True
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif answer.isdigit():
            answer = int(answer)

            os.system('cls' if os.name == 'nt' else 'clear')
            print("Компания: " + companyList[answer - 1]["name"])
            print("Стоимость одной акции: " + str(companyList[answer - 1]["price"]))
            print("Акций у вас на руках: " + str(companyList[answer - 1]["purchased"]))
            print("")
            print("Ваши деньги: " + str(round(money, 2)))
            print("")

            while True:
                if flag2 == True:
                    break

                print("Введите количество акций, которое хотите купить или 0 для отмены покупки")
                #Сколько акций хотим купить
                buyAnswer = input()


                if buyAnswer == "0":
                    isEnd = True
                    flag = True
                    break
                elif buyAnswer.isdigit():
                    buyAnswer = int(buyAnswer)
                    print("")
                    print("Подтвердите покупку " + str(buyAnswer) + " акций на сумму " + str(round(buyAnswer * companyList[answer - 1]["price"], 2)))
                    print("*да* для подтверждения, *нет* для отмены")
                    

                    while True:
                        confirmationAnswer = input()

                        if confirmationAnswer == "да":
                            if money >= round(buyAnswer * companyList[answer - 1]["price"]):
                                companyList[answer - 1]["purchased"] += buyAnswer
                                money -= buyAnswer * companyList[answer - 1]["price"]
                                flag2 = True
                                print("")
                                print("Акции приобретены!")
                                break
                            elif money < round(buyAnswer * companyList[answer - 1]["price"]):
                                print("У вас не хватает денег для покупки")
                                flag2 = True
                                break

                        elif confirmationAnswer == "нет":
                            isEnd = True
                            os.system('cls' if os.name == 'nt' else 'clear')
                            flag2 = True
                            break

                        else:
                            print("Неправильный ввод, повторите еще раз")
                            print("")
                    break
                
                else:
                    print("Неправильный ввод, повторите еще раз")
                    print("")
        else:
            print("Некорректный ввод, повторите ввод")
            print("")


    

    else:
        isEnd = True
        os.system('cls' if os.name == 'nt' else 'clear')


    if isEnd == False:
        print("0. Назад")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    if isEnd == True:
        os.system('cls' if os.name == 'nt' else 'clear')

    return money

