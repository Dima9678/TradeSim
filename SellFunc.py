import os
import time

from Companys import companyList
from GlobalVariables import money



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