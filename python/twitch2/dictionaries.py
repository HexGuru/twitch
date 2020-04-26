


# Dictionaries are also known as Maps in other languages
# Keys are associated to Values, and are separated by a ':'
students_ids = {
    'Gabrio' : 196653,
    'Mike' : 123123,
    'Simran' : 44485,
    'Amraan' : 21344243
}

students_marks = {
    196653 : {
        "Math": 8,
        "History" : 5,
    },
    123123 :{
        "Math": 8,
        "History" : 8,
    },
    44485 :{
        "Math": 8,
        "History" : 11,
    },
    21344243 :{
        "Math": 9,
        "History" : 7,
    },
}

def main():
    # You can access the values of the dictionary in two different ways
    print(students_ids['Simran'])
    print(students_ids.get('Mike'))
    
    # We can also access all the available keys and values in a dictionary
    print(students_ids.keys())   # DICT.keys() returns the list of keys
    print(students_ids.values()) # DICT.values() returns the list of values
    print(students_ids.items())  # DICT.items() returns a list of touples in the form ( key, value )

    # How to navigate information across different dictionaries:
    username = input("Whats your name: ")
    userid = students_ids[username]
    print("Your grades follow:")
    for grade in students_marks[userid].items():
        print(grade[0], grade[1])

    print("print just the student names")
    for student_names in students_ids.keys():
        print(student_names)


main()