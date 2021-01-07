import random

class Game:
    def __init__(self, options):
        self.options = options
        self.count = len(options)
        print('Game started')

    def computer_choose(self):
        random_option = random.randint(0, self.count - 1)
        self.options[random_option].set_opted(True)
        print('We choose the option: ')

    def your_choose(self):
        chosen_option = int(input('Choose your option: [1 - %s] ' % self.count))
        self.chosen_option = chosen_option - 1
        self.options[chosen_option - 1].set_chosen(True)
        print('You choose the option: %s %s' % (chosen_option, ''))

    def open_choose(self):
        print(self.options[self.chosen_option].is_opted)


class User:
    is_opted = False
    is_chosen = False

    def set_opted(self, is_opted):
        self.is_opted = is_opted

    def set_chosen(self, is_chosen):
        self.is_chosen = is_chosen


game = Game([User(), User(), User()])
game.computer_choose()
game.your_choose()
game.open_choose()