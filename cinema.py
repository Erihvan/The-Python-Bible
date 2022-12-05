
# we create a film dictionary with its own dictionary that has age and seat number:

films = {
    "Finding Dory": [3,5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5],
    }

# here, we are telling the code to make a loop with "while True" and a variable named "choice"
# the variable "choice" is asking wich film would you like to see and also by adding ".strip()" y eliminating any space and ".title()" is capitalizing any lowercase input in order to search for the movie input inside the dictionary
# then we tell the code that "if" input "choice" is True inside "films" dictionary then go on "pass" but if is not then print "we dont have that film"
while True:
    choice = input("What film would you like to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())

        # Check user age
        if age >= films[choice][0]:
            # Check enough seats

            num_seats = films[choice][1] #create a variable that gives you the number of seats from the input "choice" inside the variable "films"
            
            if num_seats > 0: # if "num_seats" is gretaer than 0 it would allow you enjoy the film
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1 # then it would substract from variable "num_seats" 1 ticket
            else:
                print("Sorry, we are sold out!") # so if the num_ of tickets is <= 0 it would print a sold out message

        else:
            print("You are too young to see that film!")
            
    else:
        print("We don't have that film...")
    
