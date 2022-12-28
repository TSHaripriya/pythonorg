'''class bank_account():
     def __init__(self,name,account_number,account_balance):
         self.name=name
         self.account_number=account_number
         self.account_balance=account_balance
     def avilable_balance(self):
         print("available balance is",self.account_balance)
     def withdraw(self,withdraw_amount):
         try:
            self.withdraw_amount = withdraw_amount
            print("Amount withdraw",self.withdraw_amount)
            if self.withdraw_amount < self.account_balance:
                self.account_balance=self.account_balance-self.withdraw_amount
                print("Amount withdraw",self.account_balance)
         except OverflowError:
            print("Withdraw is greater than available balance")
obj=bank_account("hari",567512,4000)
obj.avilable_balance()
obj.withdraw(100)'''


class bank_account():
    def __init__(self, name, account_number, account_balance):
        self.name = name
        self.account_number = account_number
        self.account_balance = account_balance

    def avilable_balance(self):
        print("available balance is", self.account_balance)

    def withdraw(self, withdraw_amount):
        try:
            self.withdraw_amount = withdraw_amount
            print("Amount withdraw", self.withdraw_amount)
            if self.withdraw_amount < self.account_balance:
                self.account_balance = self.account_balance - self.withdraw_amount
                print("Amount withdraw", self.account_balance)
        except OverflowError:
            print("Withdraw is greater than available balance")


obj = bank_account("hari", 567512, 4000)
obj.avilable_balance()
obj.withdraw(100)





