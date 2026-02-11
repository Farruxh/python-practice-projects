import random
import string

char_values = string.ascii_letters + string.digits 

len = int(input("Enter the length of the password : "))

# password using loop
password_loop = ""
for i in range(len):
    password_loop += random.choice(char_values)
print(password_loop)

# password using list comprehension and join func
password_lis_comp = "".join([random.choice(char_values) for i in range(len)])
print(password_lis_comp)