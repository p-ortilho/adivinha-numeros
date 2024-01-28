import random
import os
from art import text2art
from colorama import Fore

init_game = ''

def menu():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    name_game = text2art('Adivinha Numeros', font='small', chr_ignore=True)
    print(Fore.GREEN + name_game + Fore.RESET)
    print(Fore.BLUE, 'Neste jogo, o seu objetivo é acertar o número gerado aleatoriamente entre 0 e 100.\n Pressione "s" (start) para começar ou "e" (exit) para sair.', Fore.RESET)
def number_generate():
    num = random.randint(1, 100)
    return num 
def game():
    number = number_generate()
    tentativas = 1

    while True:
        input_number = input(' Digite um número: ')
        if not input_number.isdigit():
            print(Fore.MAGENTA, 'O valor digitado não é um número!', Fore.RESET)
        elif number == int(input_number):
            print(Fore.GREEN, 'Você acertou!', Fore.RESET)
            print(Fore.YELLOW, f'Número de tentativas: {tentativas}', Fore.RESET)
                
            init_new_game = input(' Gostaria de jogar novamente? Digite "s" (start) para começar ou "e" (exit) para sair.\n ').lower()
            if init_new_game == 's':
                game()
            else:
                exit()
        elif number > int(input_number):
            print(Fore.RED, 'Digite um número maior.', Fore.RESET)
        elif number < int(input_number):
            print(Fore.CYAN, 'Digite um número menor.', Fore.RESET)
        tentativas += 1  
menu()

while init_game not in ['s', 'e']:
    init_game = input('\n Digite uma opção: ').lower()

if init_game == 's':
    game()
else:
    exit()