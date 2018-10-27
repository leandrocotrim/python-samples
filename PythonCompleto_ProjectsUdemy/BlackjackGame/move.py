from player import Player

class Move(object):
    '''Move in Blackjack game'''

    _player = None

    def __init__(self, player):
        self._player = player