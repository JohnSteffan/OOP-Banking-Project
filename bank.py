class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        #self.custID = 
        self.accounts = []
        #self.creditcards = []
        self.services = []


    def get_credit_score(self):
        self.credit_score = 850 if self.firstname == 'John' else 700




class Account:
    def __init__(self, type, number):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance