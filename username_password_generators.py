# Each employee’s user name is generated by taking the first five letters of their last name.

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
print(new_account) # Villa


# Temporary passwords are also generated from their last names by creating a slice out of 
# the third through sixth letters of last_name. Your string should have a total of 4 characters.

temp_password = last_name[2:6]
print(temp_password) # llan





# The Company has realized that their policy of using the first five letters of an 
# employee’s last name as a user name isn’t ideal when they have multiple employees with the same last name.


# Function account_generator takes two inputs, first_name and last_name and concatenates 
# the first three letters of each and then returns the new account name.

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  return first_name[0:3] + last_name[0:3]

new_account = account_generator(first_name, last_name)
print(new_account) # JulBle


# Function password_generator takes two inputs, first_name and last_name and then 
# concatenate the last three letters of each and returns them as a string.


# Function password_generator takes two inputs, first_name and last_name and then 
# concatenate the last three letters of each and returns them as a string.

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)
print(temp_password) # ikouki




# This was my first try at password_generator: Not the expected results.

def password_generator_bad(first_name, last_name):
  return str(first_name[len(first_name)-3:len(first_name)-1]+ last_name[len(first_name)-3:len(last_name)-1])

first_name = "Julie"
last_name = "Blevins"

temp_password_bad = password_generator_bad(first_name, last_name)
print(temp_password_bad) # lievin

# Compare:
temp_password_Julie = password_generator(first_name, last_name)
print(temp_password_Julie) # liens
