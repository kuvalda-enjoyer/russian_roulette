from strings import *
from random import shuffle
from time import sleep

def printing(txt, fast=False):
    if not fast:
        for i in txt:
            sleep(0.05)
            print(i, end='', flush=True)
    else:
        for i in txt:
            sleep(0.005)
            print(i, end='', flush=True) 

printing(f'{split_}{hello}{split_}', fast=True)
sleep(1)
printing(f'{rules}\n')

while (num := input(f'{choose_number_of_rounds}')) != "0":
    if int(num)>5:
        printing('Your number is more than 5!\n')
        continue
    load = [1]*int(num) + [0]*(6-int(num))
    shuffle(load)
    printing('Rounds are loaded. Press Enter to shoot')
    is_alive = True
    for i in range(6-int(num)):
        input()
        sleep(1)
        if load[i] == 1:
            printing(f'\n{shoot}')
            is_alive = False
            break
        else:
            printing(f'\n{no_shoot}')
    
    sleep(1)
    if is_alive:
        printing('\nYou have won!')
        printing(WINNER, fast=True)
    else:
        printing('\nYou have lost.')
        printing(LOSER, fast=True)
    printing(f'\n{new_game}\n')
    input()
printing('Goodbye, player!')
sleep(1)