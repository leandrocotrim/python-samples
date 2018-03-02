#import pymongo
from pymongo import MongoClient

class Dao:
    '''
    Class Dao to mongo
    '''
    __client = None

    def __init__(self):
        '''
        constructor
        '''
        self.__client = MongoClient('localhost', 27017)

    def save(self):
        '''
        Save object        
        '''
        return self.__client

