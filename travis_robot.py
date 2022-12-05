known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

# "len" function counts all the elements inside a table

# "while" function makes a loop of a command or in other words, runs it indefinitively
while True:
    print("Hi! My name is Travis")
    
# we use function like "strip" to eliminate any missing space that can cause us a issue on our code and also
# we use function "capitalize" in order to make capitalized the first letter of our input "name" an avoid any user error

    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
# here we use the "format" function in order to tell the code to place inside the brakets "{}" the name and make a whole sentence "Hello (name)!"
        print("Hello {}!".format(name))

# now our code has recognised the name, it would ask us if we would like to be removed from sistem
# make a variable asking "Would you like to be removed?

        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        
# so, by using "if" function we are conditioning the task to be executed if is "True"
# "or" funtion tells code to execute it either if its "y" or "Y" would always be "True" answer
         #if remove == "y" or remove == "Y"
# BUUUUUUT.... instead of using all the code above, lets just lower case the input by using "lower()"

        if remove == "y" :
             # to remove from list just use "list.remove()" method
             known_users.remove(name)
        elif remove == "n":
             print("No problem, I didn't want you to leave anyway!")
             
# we use "else" to tell code that if name is "False" or not recognized be able to print "name NOT recognised"
    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_me = input ("Would you like to be added to the system (y/n)?: ").strip().lower()
# so here we are telling the prigram to ask if the name is not added into the list "known_names" would you like to be added?
#If the answer is "yes" then the system would add you to the list by the "append" method.
        if add_me == "y":
# Now we use de "append" method to add names in the "known_users" list fro example:
            known_users.append(name)
        elif remove == "n":
            print("No worries, see you arround!")
        
