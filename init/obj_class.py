class Cotrim:
    '''
    class de teste
    '''
    __name = ''

    def __init__(self, name):
        '''
        constructor
        '''
        self.__name = name
    
    def get_name(self):
        return self.__name


c = Cotrim('leandro')
print(c.get_name())