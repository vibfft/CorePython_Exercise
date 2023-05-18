import sys
import random

invite_number = int(input("Enter the number of friends joining (including you):\n"))
if invite_number <= 0:
    print("No one is joining for the party")
    sys.exit(1)

friends_list = []
print("Enter the name of every friend (including you), each on a new line:")
for i in range(invite_number):
    friends_list.append(input().strip())
    
# print(friends_list)
bill = int(input("Enter the total bill value:\n"))

indiv_bill = 0
if not (bill % invite_number):
    indiv_bill = int(bill/invite_number)
else:
    indiv_bill = float(bill/invite_number) 
# print(f"indiv bill: {indiv_bill}")
friends_number = [round(indiv_bill,2)]*invite_number

friends_dict = dict(zip(friends_list, friends_number))


yes_or_no = input('Do you want to use the "Who is lucky?" feature?  Write Yes/No\n')

if yes_or_no.strip() == 'No':
    print("No one is going to be lucky")
    print(friends_dict)
else:
    random_key = random.choice(list(friends_dict.keys()))
    print(f"{random_key} is the lucky one!")
    indiv_bill = 0
    if not (bill % invite_number - 1):
        indiv_bill = int(bill/(invite_number - 1))
    else:
        indiv_bill = float(bill/(invite_number - 1))
        
    friends_number = [round(indiv_bill,2)]*invite_number

    friends_dict = dict(zip(friends_list, friends_number))
    friends_dict[random_key] = 0
    print(friends_dict)
    