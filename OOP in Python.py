#                   1. classes and objects
# class computer:
#     def config(self):
#         print('i5 , 16gb, 512gb')

# a = 5

# com1 = computer()                 # com1 is object of class computer
# com2 = computer()                 # objects can be many of single class
# computer.config(com1)             # two different ways for using class methods - by class name
# com2.config()                     # by object name
# #print(type(com1))                #output - <class '__main__.computer'>


#                   2. __init__ method  - special method

class computer:
    def __init__(self,cpu,ram):                 #  passing values in class
        self.cpu = cpu
        self.ram = ram                          #  class variable
    def config(self):
        print(self.cpu,self.ram)                # printing class variable values

com1 = computer('i5','16')
com2 = computer('i5','8')
com1.config()
com2.config()