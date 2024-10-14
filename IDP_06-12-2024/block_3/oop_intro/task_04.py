# -*- coding: utf-8 -*-

'''
Создайте класс BankAccount с атрибутами balance и owner. Добавьте методы deposit и withdraw для пополнения и снятия
денег со счета.
'''


class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.balance = initial_balance
        self.owner = owner

    def deposit(self, money):
        self.balance += money
        return self.balance

    def withdraw(self, money):
        self.balance -= money
        return self.balance


bank_account = BankAccount(owner="Ivan", initial_balance=50000)

money_to_deposit = 100
print(bank_account.deposit(money_to_deposit))
money_to_withdraw = 10000
print(bank_account.withdraw(money_to_withdraw))
