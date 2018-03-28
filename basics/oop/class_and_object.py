class Demo:
    # constructor
    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum
    
    def display(self):
        print "name:", self.name, ", id: ", self.idnum
        
obj1 = Demo('Sam', '123456')     
obj1.display()


class Demo_2:
    # constructor with pre-assigned value
    def __init__(self, name, idnum=10):
        self.name = name
        self.idnum = idnum
    
    def display(self):
        print "name:", self.name, ", id: ", self.idnum
        
obj2 = Demo_2('Sam')     
obj2.display()
