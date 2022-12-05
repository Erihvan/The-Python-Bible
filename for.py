numbers = {
    "list_1": ["98254", "98944", "19834", "294385", "29430"],
    "list_2": ["2109402", "130", "12903", "294430", "10394"]
    }

for key in numbers.keys():
    for number in numbers[key]:
        if "0" in number:
            print(number)
