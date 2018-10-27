from card import Card

class Deck(object):
    '''Helper of Deck'''

    __symbols = ['♣', '♥', '♠', '♦']
    __tp_cards = [('A', 1)] + [(str(i), i) for i in range(2, 11)] + [('J', 10), ('Q', 10), ('K', 10)]
    _cards = None


    def __init__(self, num):
        self._cards = [Card(c, v, num, s) for c, v in self.__tp_cards for s in self.__symbols]


    def __str__(self):
        return "\n".join([str(c) for c in self._cards])
