#Graded: 13/14
#Jing Yi Hon
#May 29, 2016
#Homework 3

#Make a list called countries with seven countries

countries = ["France", "Bhutan", "The United Kingdom", "Taiwan", "Singapore",
"New Zealand"]

#TA-STEPHAN: Needs to be seven courtries, not six.

#Using a for loop, print each element of the list

for country in countries:
    print(country)

#Sort the list permanently
#TA-STEPHAN: No need to print countries.sort().
print(countries.sort())
print(countries)

#Display the second-to-last element of the list using a line of code that will
#work no matter what the size of the list is. (hint: len will be helpful)

print(countries[-2])

#Delete one of the countries from the list using its name

countries.remove("Singapore")

#Using a for loop, print each element of the list again, which should now be one
#element shorter
print("______")
for country in countries:
    print(country)

#Dictionaries
#Make a dictionary called 'tree' that responds to name, species, age,
#location_name, latitude and longitude. Pick a tree.

tree = {"name": "Queen Elizabeth Oak", "species": "Sessile Oak", "age": 1000,
"location_name": "Cowdray Park, West Sussex, England", "latitude": 50.9871,
"longitude": -0.7321}

#Print the sentence "{name} is a {years old} tree that is in {location_name}"

print(tree["name"], "is a", tree["age"], "years old tree that is in",
tree["location_name"])

#The coordinates of NYC are 40.7128 degrees N, 74.0059 degrees W. Check to see
#if the tree is south of NYC and print "The tree {name} in {location} is south
#of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"

if tree["latitude"] < 40.7128:
    print("The tree", tree["name"], "in", tree["location_name"], "is south of NYC")
else:
    print("The tree", tree["name"], "in", tree["location_name"], "is north of NYC")

#Ask the user how old they are. If they are older than the tree, display "you are"
#{X}years older than {name}." iF they are younger than the tree, display "{name} was"
#{X} years old when you were born.

age = (input)("How old are you?")
if int(age) > tree["age"]:
    age = int(age) - tree["age"]
    print("You are", age, "years older than", tree["name"])
else:
    age = tree["age"] - int(age)
    print(tree["name"], "was", age, "years old when you were born")


#Make a list of dictionaries of five places across the world -
#(1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago.
#Each dictionary should include each city's name and latitude/longitude

world = [
    {"name": "Moscow", "latitude": 55.7558, "longitude": 37.6173},
    {"name": "Tehran", "latitude": 35.6892, "longitude": 51.3890},
    {"name": "Falkland Islands", "latitude": -59.7163, "longitude": -59.5236},
    {"name": "Seoul", "latitude": 37.5665, "longitude": 126.9780},
    {"name": "Santiago", "latitude": -33.4489 , "longitude": -70.6693},
]

#Loop through the list, printing each city's name and whether it is above or
#below the equator (How do you know? Think hard about the latitude.)
#When you get to the Falkland Islands, also display the message
#"The Falkland Islands are a biogeographical part of the mild Antarctic zone,"
#which is a sentence I stole from Wikipedia.
#Loop through the list, printing whether each city is north of south of your
#tree from the previous section.
#Loop through the list, printing whether each city is north of south of your
#tree from the previous section.

for city in world:
    if city["latitude"] > 0:
        print(city["name"], "is above the equator")
    if city["latitude"] < 0:
        print(city["name"], "is below the equator")
    if city["name"] == "Falkland Islands":
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")
    if city["latitude"] > tree["latitude"]:
        print(city["name"], "is north of", tree["name"])
    if city["latitude"] < tree["latitude"]:
        print(city["name"], "is south of", tree["name"])
