class OscarsWinners:
    def __init__(self,index,year,age,name,movie):
        self.__index = index
        self.__year = year
        self.__age = age
        self.__name = name
        self.__movie = movie
    
    def getIndex(self):    
        return self.__index
    
    def getYear(self):    
        return self.__year
    
    def getAge(self):    
        return self.__age
    
    def getName(self):    
        return self.__name
    
    def getMovie(self):    
        return self.__movie