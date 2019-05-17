from loto_base import Card
from loto_base import Player
from loto_base import Bag
from loto_base import print_card
from sys import exit as stop

bag = Bag()
bag = bag.create_bag()

card = Card()
card1 = card.create_card()
card2 = card.create_card()

player1 = Player()
player2 = Player()

p1 = 0
p2 = 0
while len(bag) != 0:
    print_card(card1, 'Ваша карточка')
    print_card(card2, 'Карточка компьютера')
    print()
    move = player1.move(bag)
    print(move[1], move[2])
    print()
    if player2.mark(card2, move[0]):
        p2 += 1
        if p2 == 15:
            print('Игра окончена. Победил компьютер...')
            stop()
    answer = input('Зачеркнуть число - [1], Продолжить - [Enter]')
    print()
    if answer == '1':
        if player1.mark(card1, move[0]):
            p1 += 1
            if p1 == 15:
                print('Игра окончена. Вы победили!!!')
                stop()
            print('Продолжаем игру:')
            print()
            continue
        else:
            print(f'Вы проиграли :( В Вашей карточке нет числа ({move[0]})')
            stop()
    elif answer == '':
        if player1.mark(card1, move[0]):
            print(f'Вы проиграли :( В Вашей карточке есть число ({move[0]})')
            stop()
        else:
            print('Продолжаем игру:')
            print()
            continue
