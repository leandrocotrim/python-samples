from player import Player, Dealer
from move import Move
from deck import Deck

import random

class Blackjack(object):
    '''Blackjack game'''

    __dealer = None    
    __dic_num_players = None
    __dic_num_decks = None
    __cards = []

    def __init__(self):
        '''Inicialize game'''
        self.__dealer = Dealer()
        self.__dic_num_players = { i : i for i in range(1, 8) }
        self.__dic_num_decks = { i : i for i in range(1, 3) }


    def __build_player(self,num_players):
        self.__players = [Player(input('Enter the name {} player: '.format(i)), i) for i in range(1, num_players + 1)]


    def __build_decks(self, num_decks):
        for num_deck in range(1, num_decks + 1):
            self.__cards.extend(Deck(num_deck)._cards)


    def __shuffle(self, num=10):
        for i in range(num):
            self.__cards = random.sample(self.__cards, len(self.__cards))


    def start(self):
        '''Start Blackjack game'''

        num_players = 0
        while num_players == 0:
            try:
                num_players = self.__dic_num_players[int(input('Enter the number of players(1-7): '))]                
            except:
                print('Invalid value number of players.')        

        self.__build_player(num_players)

        num_decks = 0
        while num_decks == 0:
            try:
                num_decks = self.__dic_num_decks[int(input('Enter the number of decks(1-3): '))]
            except:
                print('Invalid value nunmber of decks.')

        self.__build_decks(num_decks)
        self.__shuffle()



blackjack = Blackjack()
blackjack.start()
