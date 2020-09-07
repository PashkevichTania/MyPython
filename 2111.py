# coding=<utf-8>
# -*- coding: utf8 -*-
from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()


def game():
    koloda = [6,7,8,9,10,2,3,4,11] * 4
    import random
    random.shuffle(koloda)
    count = [0,0]
    n = 0
    while n <= 1:
        print(colored('Готовьтесь', 'red', 'on_white'))
        s = n + 1
        print(colored('player %d'  %s, 'cyan'))
        while True:
            choice = input('Будете брать карту? y/n\n')
            if choice == 'y':
                current = koloda.pop()
                print('Вам попалась карта достоинством ', current)
                count[n] += current
                if count[n] > 21:
                    print(colored('''Извините, но вы проиграли, У вас %d очков''' %count[n], 'red'))
                    break
                elif count[n] == 21:
                    print(' вы набрали 21!')
                    break
                else:
                    print('У вас {} очков, playr {}'.format(count[n], s))
            elif choice == 'n':
                print(colored('У вас %d очков и вы закончили игру.' %count[n], 'cyan'))
                break
        n += 1
    res = 0
    chemp = 0
    n = 0
    if count[0] == count[1]:
        print('ничья')
    else:
        while n<2:
            if res < count[n] and count[n] < 21:
                res = count[n]
                chemp = n + 1
            n += 1
        print(colored('player %d WIN' %chemp, 'blue', 'on_yellow'))
    #count = [0,0]
    restart()
def restart():
    choice = input('ЕЩЕ РАЗ? y/n\n')
    if choice == 'y':
        game()
    else:
        print(colored('конец', 'red', 'on_white'))
game()
