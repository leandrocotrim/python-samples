class Player(object):
    '''Class Player of Blackjack game'''

    _name = None
    _number = -1

    def __init__(self, name, number):
        '''Inicialize Player in Blackjack game'''
        self._name = name
        self._number = number


class Dealer(Player):
    '''Class Dealer of Blackjack game'''

    def __init__(self, name='Dealer', number=0):
        '''Inicialize Player in Blackjack game'''
        super().__init__(name, number)