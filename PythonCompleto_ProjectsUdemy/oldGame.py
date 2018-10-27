from functools import reduce


class OldGame(object):
    '''OldGame in Python'''

    def __init__(self):
        '''Init of OldGame'''
        self.__reset()
        
        
    __table = None
    __gamers = { 'X', 'O' }
    __gamer = None
    

    def __reset(self):
        self.__table = [[1,2,3],[4,5,6],[7,8,9]]


    def __print_table(self):
        for l in self.__table:
            print('{}|{}|{}'.format(l[0], l[1], l[2]))
    

    def __winer(self):
        rows = [ (l[0] == l[1] and l[1] == l[2])  for l in self.__table ]
        cols = [ (self.__table[0][c] == self.__table[1][c] and self.__table[1][c] == self.__table[2][c]) for c in range(3) ]
        diagonals = [ (self.__table[0][0] == self.__table[1][1] and self.__table[1][1] == self.__table[2][2]), 
                      (self.__table[2][0] == self.__table[1][1] and self.__table[1][1] == self.__table[0][2]) ]

        return sum([sum(rows), sum(cols), sum(diagonals)]) > 0
        

    def __set_position(self, position):
        for iline, line in enumerate(self.__table):            
            for icol, col in enumerate(line):                
                if str(col) == position:                    
                    self.__table[iline][icol] = self.__gamer
                    return True
        return False


    def __run(self):
        while True:
            print('\nFirst gamer is {}'.format(self.__gamer))

            winer = position = None
            while winer is None:        
                self.__print_table()

                position = input('\nGamer "{}" type one position: '.format(self.__gamer)).upper()
                if position == 'EXIT': break
                
                if not self.__set_position(position): 
                    print('Position invalid.')
                    continue

                if self.__winer():
                    print('\n\nGamer winer is "{}"'.format(self.__gamer))
                    self.__reset()
                    break

                self.__gamer = reduce(lambda acc, g: g if g != self.__gamer else acc, self.__gamers)
            
            if position == 'EXIT': break


    def start(self):
        while self.__gamer is None:
            gamer = input('Type first gamer X or O: ').upper()            
            if gamer in self.__gamers: 
                self.__gamer = gamer
        
        print('Any time type "exit" for exit.')

        self.__run()


old_game = OldGame()
old_game.start()