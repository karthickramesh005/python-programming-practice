# Abstrac Base Class :

from abc import ABC ,abstractmethod

class bank(ABC):
    @abstractmethod
    def loan(self):pass
    
    @abstractmethod
    def credit(self):pass
    
    @abstractmethod
    def debit (self):pass

class HDFC(bank):
    def loan(self):
        print("we can ptovide 7.5 % Intrest Loan ")

    def credit(self):
        print("HDFC provide credit")

    def debit (self):
        print("HDFC provide Dedit")

    # additional
    def card(self):
        print("HDFC provide multiple cards")


o= HDFC()
o.loan()
o.credit()
o.debit()
o.card()
