# import datetime

# today = datetime.date.today()
# current_year = today.year

# birth_year = input("What year were you born? ")
# print(f"Your age is {int(current_year) - int(birth_year)}")

username = input("Username: ")
password = input("Password: ")

password = "*" * len(password)

print(f"Your username is {username} and your password is {password} and it's {len(password)} long")

lst = [1,3,5]
lst.clear()
print(lst)