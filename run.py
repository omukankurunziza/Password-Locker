#!/usr/bin/env python3.6

from account import Account

    def create_account(account_name,user_name,password):
        '''
        Function to create a new account
        '''
        new_account = Account(account_name,user_name,password)
        return new_account

    def save_accounts(account):
        '''
        Function to save account
        '''
        account.save_account()

    def del_ account( account):
        '''
        Function to delete a  account
        '''
         account.delete_ account()

    def find_account(account_name):
        '''
        Function that finds a account by account_name and returns the account
        '''
        return Account.find_by_account_name(account_name)

    def check_existing_accounts(account_name):
        '''
        Function that check if a account exists with that account_name and return a Boolean
        '''
        return Account.account_exist(account_name)

    def display_accounts():
        '''
        Function that returns all the saved accounts
        '''
        return Account.display_accounts()