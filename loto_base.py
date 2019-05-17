import random

class Player:                    
    def move(self, bag):
        bar = random.choice(bag)
        bag.remove(bar)
        return bar, f'Новый бочонок: ({bar})', f'(Осталось: {len(bag)})'
    
    def mark(self, card, bar):
        for line in card:
            for num in line:
                if num == bar:
                    line.insert(line.index(num), '-')
                    line.remove(num)
                    return True
                    break

class Card:
    @staticmethod
    def _raw_card():        
        card = []        
        ints_start = [i + 1 for i in range(1, 9)]
        column = sorted(random.sample(ints_start, 3))
        card.append(column)                
        a = 10
        b = 20
        for _ in range (7):
            ints = [i + 1 for i in range(a - 1, b - 1)]
            column = sorted(random.sample(ints, 3))
            card.append(column)
            a += 10
            b += 10                    
        ints_end = [i + 1 for i in range(79, 90)]
        column = sorted(random.sample(ints_end, 3))
        card.append(column)                
        card = list(map(list, zip(*card)))                
        for line in card:
            spaces = random.sample([i + 1 for i in range(0, 8)], 4)
            for f in spaces:
                line.pop(f)
                line.insert(f, '')
        return list(map(list, zip(*card)))
    
    def create_card(self):
        card = Card._raw_card()
        i = 0
        while i < 8:
            for line in card:    
                if str(line[0]) + str(line[1]) + str(line[2]) == '':
                    card = Card._raw_card()
                    i = 0
                    break
                else:
                   i += 1
        return list(map(list, zip(*card)))



class Bag:
    def create_bag(self):
        return [i + 1 for i in range(90)]

        
def print_card(card, name): 
    name = name.ljust(int((35 - len(name)) / 2 + len(name)), '-')
    name = name.rjust(35, '-')
    print(name)
    for line in card:
        for i in line:
            print('{:3}'.format(str(i)), end = ' ')
        print()
    print(''.ljust(35, '-'))


