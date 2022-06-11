username = input()
password = input()
new_pass = input()
while new_pass != password:
    new_pass = input()
print(f"Welcome {username}!")