import random
import time

player_score = 0
computer_score = 0

#основной цикл
def main():
    global player_score, computer_score
    while True:
        choice = input("Выбери действие \n1 камень\n2 ножницы\n3 бумага\nq выход")
        #логика и вывод
        if choice == "1" or choice == "2" or choice == "3":
            print("ход компьютера")
            time.sleep(1)
            choice_computer = random.randint(1,3)
            if choice_computer == 1:
                print("компьютер выбрал камень🪨")
                time.sleep(1)
            elif choice_computer == 2:
                print("компьютер выбрал ножницы✂️")
                time.sleep(1)
            elif choice_computer == 3:
                print("компьютер выбрал бумагу📜")
                time.sleep(1)
            # Сравнение выборов
            if int(choice) == choice_computer:
                print("Ничья!")
            elif (int(choice) == 1 and choice_computer == 2) or \
                    (int(choice) == 2 and choice_computer == 3) or \
                    (int(choice) == 3 and choice_computer == 1):
                print("Ты победил!🥳")
                player_score += 1
            else:
                print("Ты проиграл!💻")
                computer_score += 1

            # Показать счёт
            print(f"Счёт: Ты {player_score} : {computer_score} Компьютер")



        elif choice == "q":
            break

        else:
            print("неправильный ввод")

if __name__ == "__main__":
    main()