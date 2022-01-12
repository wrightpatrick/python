x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
print(x)
x[1][0] = 15
# students[1] = 'Bryant'
sports_directory["soccer"][0] = 'Andres'
z[0]['y'] = 30

print(x)
# print(students)
print(sports_directory["soccer"])
print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(dictionary):
    for x in range(0, len(dictionary), 1):
        print(dictionary[x])

iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_  name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, value_list):
    for x in range(0, len(value_list), 1):
        print(value_list[x][key_name])

iterateDictionary2('first_name', students)

def iterateDictionary3(key_name, value_list):
    for x in range(0, len(value_list), 1):
        print(value_list[x][key_name])

iterateDictionary3('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# length_key = len(dojo['locations'])
# print (length_key, "loactions")
# i = 0
# while


# while


def printInfo(dictionary):
    for x in range(0, len(dictionary), 1):
        print(f"{len(dictionary['locations'])} LOCATIONS")
        for y in range(0, len(dictionary['locations']), 1):
            print(dictionary['locations'][y])
        # print(dictionary['locations'])
        print(f"{len(dictionary['instructors'])} INSTRUCTORS")
        for i in range(0, len(dictionary['instructors']), 1):
                print(dictionary['instructors'][i])


printInfo(dojo)
