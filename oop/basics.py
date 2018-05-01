# Class and Object

# Student is a class, it has two instance variables: one is name, the other is
#   score. Name is a string, score is a floating point.
class Student(object):
    # __init__ is the constructor of class Student. It is used to create a new
    #   object of the class.
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    @property
    def getName(self):
        return self.__name
    def getScore(self):
        return self.__score

    # eatLunch is the way students have lunch
    def eatLunch(self):
        print("{0} is having lunch".format(self.getName))
    
        

# declared two objects s1 and s2.
s1 = Student("Romeo", 78.9)
s2 = Student("Juliet", 91.5)


# print the name and score of s1
# print(s1.name, s1.score)
s1.eatLunch()
s2.eatLunch()


