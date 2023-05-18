#!/usr/bin/env python3

players = []
num_pencils = int(input("How many pencils would you like to use:\n"))
first_player = input("Who will be the first (John, Jack):\n")

if first_player == 'John':
    players = ['John', 'Jack']
else:
    players = ['Jack', 'John']
    
print(f"{'|'*num_pencils}")
remove_pencil = int(input(f"{first_player}'s turn:\n"))
num_pencils = num_pencils - remove_pencil

index = 0
while num_pencils > 0:
    print(f"{'|'*num_pencils}")
    
    if index % 2 == 0:
        remove_pencil = int(input(f"{players[1]}'s turn:\n"))
    else: 
        remove_pencil = int(input(f"{players[0]}'s turn:\n"))
    num_pencils = num_pencils - remove_pencil
    index += 1

    