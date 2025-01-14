import os
import time

from Companys import companyList
from GlobalVariables import money



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