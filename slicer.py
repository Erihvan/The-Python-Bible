# get user email adress
email = input("what is your email address? ").strip()

# slice out user name
user = email[0:email.index("@")]

# slice domain name
domain = email[email.index("@")+1::1]

# format message
output = "Your username is {} and your domain is {}".format(user, domain)
 
# display output message

print(output)
