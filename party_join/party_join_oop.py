#!/usr/bin/env python3


import sys
import random

class PartyJoin:
    
    def __init__(self, members: int) -> None:
        self.members = members
        self.bill = 0.0
        self.friends_list = []
        self.friends_dict = {}
    
    def member_names(self) -> list:
        print("Enter the name of every friend (including you), each on a new line:")
        try:
            for i in range(self.members):
                self.friends_list.append(input().strip())
                
        except ValueError as ve:
            print("Please enter base 10 integer")
        
    def bill_split(self, lucky: bool):
        
        if lucky:
            self.members -= 1
            
        indiv_bill = 0
        if not (self.bill % self.members):
            indiv_bill = int(self.bill/self.members)
        else:
            indiv_bill = float(self.bill/self.members) 
        friends_number = [round(indiv_bill,2)]*self.members
        self.friends_dict = dict(zip(self.friends_list, friends_number))
        
    def total_bill(self):
        
        try:
            self.bill = int(input("Enter the total bill value:\n"))
            self.bill_split(False)
            
        except ValueError as ve:
            print("Please enter base 10 integer")

    def whos_lucky(self):
        yes_or_no = input('Do you want to use the "Who is lucky?" feature?  Write Yes/No\n')

        try:
            if yes_or_no.strip() == 'No':
                print("No one is going to be lucky")
                print(self.friends_dict)
            else:
                random_key = random.choice(list(self.friends_dict.keys()))
                print(f"{random_key} is the lucky one!")
                self.bill_split(True)
                self.friends_dict[random_key] = 0
                print(self.friends_dict)
                
        except ValueError as ve:
            print("Please enter 'Yes' or 'No'")
    
def main() -> None:

    invite_number = 0
    try:
        invite_number = int(input("Enter the number of friends joining (including you):\n"))
        if invite_number <= 0:
            print("No one is joining for the party")
            sys.exit(1)
            
    except ValueError as ve:
        print("Please enter base 10 integer")
        sys.exit(1)
        
    p = PartyJoin(invite_number)
    p.member_names()
    p.total_bill()
    p.whos_lucky()
    
if __name__ == '__main__':
    main()