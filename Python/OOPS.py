# Sample class Student
class Student:
    SName = "Mahua"
    SRollNo = 13
    def displayDetails(self):
        print("Name is:",self.SName)
        print("RollNo is:",self.SRollNo)
Std1 = Student()
#Std1.displayDetails()
#print(Std1.SName)
#print(Std1.SRollNo)


'''
# Constructor
class Constructor:
    SName = "Aastha"
    SRollNo = 1
    def __init__ (self,sroll,sname):
        self.SName = sname
        self.SRollNo = sroll
    def displayDetails(self):
        #Printing Class Variables
        print(self.SName)
        print(self.SRollNo)
    #def showInstance(self):
        # Printing Instance Variables
    #    print()


print(Constructor.SName)
print(Constructor(2,"Abhijeet").SName)
Std2 = Constructor(14,"Mayank")
#Std3 = Constructor()

Std2.displayDetails()
#Std3.displayDetails()

'''

'''
# Constructor
class Constructor:
    # Class Attributes
    SName = "Aastha"
    SRollNo = 1
    def __init__ (self,sroll,sname):
        self.IName = sname
        self.IRollNo = sroll
    def showClass(self):
        #Printing Class Variables
        print(self.SName)
        print(self.SRollNo)
    def showInstance(self):
        # Printing Instance Variables
        print(self.IName)
        print(self.IRollNo)

Std2 = Constructor(14,"Mayank")
Std2.showClass()
Std2.showInstance()
'''
'''
class BankAccount(object):
    def __init__(self, deposit):
        self.amount = deposit

    def withdraw(self, amount):
        self.amount -= amount

    def deposit(self, amount):
        self.amount += amount

    def balance(self):
        return self.amount

# Let me create an instance of 'BankAccount' class with the initial
# balance as $2000.
myAccount = BankAccount(2000)

# Let me check if the balance is right.
print (myAccount.balance())

# Let me deposit my salary
myAccount.deposit(10000)

# Let me withdraw some money to buy dinner.
myAccount.withdraw(15)

# What's the balance left?
print (myAccount.balance())
'''
# Attributes

class DataEncapsulation:
    private = 0
    protected = 0
    def __init__ (self,num1,num2,num3):
        self.public = 0 # Class Variable
        self.public = num1 # Instance Variable
        self._protected = num2
        self.__private = num3
Val = DataEncapsulation(10,20,30)
print("Public",Val.public)
print("Protected",Val._protected)
print(Val.public,Val.protected,Val.private)
print("Private",Val.__private)

