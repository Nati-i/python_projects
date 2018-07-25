correct_password = "python123"
name = input('Enter name: ')

password = input("Enter Password: ")

while correct_password != password:
    password = input("Enter again: ")

print("Hi {} Logged in".format(name))
