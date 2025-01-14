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
        print(f"{j}. {i['name']}")
        print(f"Стоимость акции: {i['price']}")
        print("")    
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











def sharesSell(money):
    flag1 = False

    os.system('cls' if os.name == 'nt' else 'clear')
    have = False

    new_company_list = []
    
    for i in companyList:
        if i['purchased'] > 0:
            have = True
            new_company_list.append(i)

    if have == True:
        print("Акции у вас на руках:")
        print("")
        j = 1 
        for i in new_company_list:
            print(f"{j}. {i['name']:<15}  Акций на руках: {i['purchased']}")
            j += 1
        print("")
        
        while True:
            print("Выберите номер акции для продажи или 0 для отмены")
            answer = input()
            

            if answer == "0":
                flag1 = True
                break
            elif answer > str(len(new_company_list) - 1):
                print("Недействительнй ввод")
                print("")
            elif answer.isdigit() and answer != "0":
                answer = int(answer)
                companyName = new_company_list[answer - 1]["name"]
                
                num = 0
                for i in companyList:
                    if i["name"] == companyName:
                        break
                    num += 1
                

                os.system('cls' if os.name == 'nt' else 'clear')

                print("Вы выбрали компанию " + companyName)
                print("Акций у вас на руках: " + str(new_company_list[answer - 1]["purchased"]))
                print("Стоимость одной акции: " + str(new_company_list[answer - 1]["price"]))
                print("")
                print("Введите количество акций, которое хотите продать или 0 для отмены")
                
                answer = input()
                if answer == "0":
                    flag1 = True
                    break
                elif answer.isdigit() and answer != "0" and int(answer) <= companyList[num]["purchased"]:
                    answer = int(answer)
                    quantity = answer
                    print("")
                    print("Подтвердите продажу " + str(answer) + " акций на сумму " + str(round(answer * companyList[num]["price"],2)))
                    print("*да* для подтверждения, *нет* для отмены")

                    while True:
                        confirmationAnswer = input()
                        if confirmationAnswer == "да":
                            money = money + round((quantity * companyList[num]["price"]), 2)
                            companyList[num]["purchased"] -= quantity
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
                elif int(answer) > companyList[num]["purchased"]:
                    print("У вас нет такого количества акций")
                    print("Неправильный ввод, повторите еще раз")
                    print("")
                else:
                    print("Неправильный ввод, повторите еще раз")
                    print("")
            else:
                print("Неправильный ввод, повторите еще раз")
                print("")


    #Если у пользователя нет купленных акций
    else:
        print("У вас нет купленных акций")

    if flag1 == False:
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
    return money
