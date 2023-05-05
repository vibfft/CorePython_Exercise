# aggregate elements from two or more iterables

usernames = ['crystal', 'sohyun', 'jason', 'eddie', 'stephen']
passwords = ['abc','def','ghi','jkl','mno']

users = dict(zip(usernames, passwords))

print(type(users))

for k, v in users.items():
    print(f"{k}: {v}")