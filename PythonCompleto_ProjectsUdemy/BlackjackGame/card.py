class Card(object):
    '''Card of Deck'''

    _name = None
    _value = None
    _symbol = None
    _num_deck = None

    def __init__(self, name, value, symbol, num_deck=0):
        '''Inincialize Card'''
        self._name = name
        self._value = value
        self._symbol = symbol
        self._num_deck = num_deck
    

    def __str__(self):
        return '{} {} {} {}'.format(self._name, self._symbol, self._value, self._num_deck)
