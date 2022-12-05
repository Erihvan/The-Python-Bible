from random import choice # we made a list of 3 questions that would be randomly selected so we tell system that "from" random "import" choice

questions = ["Why do you love to fish?: ", 
                      "Who is your mom?: ",
                      "Whats your name?: "] #now er write our 3 questrions in a string inside a variable called "questions"

questions = choice(questions) # now we tell "choice" to select a question from variable "questions" and 
answer = input(questions).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()
    
print ("Oh... Okay")
