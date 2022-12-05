
# We can combine dictionaries with lists by using squared brackets inside each key for ezample
# instead of just having the age we would put a list inside each key with: student ID, age and grade

# students = {
   # "Alice": ["ID0001", 26, "A"],
  #  "Bob": ["ID0002", 27, "B"],
  #  "Claire": ["ID0003", 17, "C"],
   # "Dan": ["ID0004", 21, "D"],
   # "Emma": ["ID0005", 22, "E"]
   #}

# So if we want to just print "claire" ID we type as we do with lists
# print(students["Claire"] [0])

# If we want to get "Dan's" age and grade we print
# print(students["Dan"] [1:])

# We can give each key its own dictonary as a value by using squiggly brackets for example:

students = {
    "Alice": {"id": "ID0001", "age": 26, "grade": "A"},
    "Bob": {"id": "ID0002", "age": 27, "grade": "B"},
    "Claire": {"id": "ID0003", "age": 17, "grade": "C"},
    "Dan": {"id": "ID0004", "age": 21, "grade": "D"},
    "Emma": {"id": "ID0005", "age": 22, "grade": "E"}
    }

# now we have a individual key for each dictionary we can search for specific data for example:
#search for "Dan's" age:
print(students["Dan"]["age"])

# what if we want "Emma's" ID and grade:
print(students["Emma"]["id"], students["Emma"]["grade"])
