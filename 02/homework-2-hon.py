#Jing Yi Hon
#May 25, 2016
#Homework 2 YAY

numbers = [22, 90, 0, -10, 3, 22, 48]

#Display the number of elements in the list
print(len(numbers))

#Display the 4th element in the list
print(numbers[3])

#Display second element plus fourth element
print((numbers[1]) + (numbers[3]))

#Display second largest element
sorted_numbers = sorted(numbers)
print(sorted_numbers[-2])

#Display last element of the original unsorted list
print(numbers[-1])

#For each number, display a number: if your original number is less than 10,
#multiply it by thirty. If it's also even, add six.
#If it's greater than 50 subtract ten. If it's not negative ten, subtract one.
#(For example: 2 is less than 10, so 2 * 30 = 60, 2 is also even,
#so 60 + 6 = 66, 2 is not negative ten, so 66 - 1 = 65.)

for number in numbers:
    if number > 10:
        print((int)(number) * 30)
        if number % 2 == 0:
            print((int)(number) + 6)
        if number > 50:
            print((int)(number) - 10)
    if number != -10:
        print((int)(number) - 1)

#Sum the result of each of the numbers divided by two.
total = 0
for number in numbers:
    new_number = number / 2
    total = total + new_number
print(total)

#Dictionary
#8) Sometimes dictionaries are used to describe multiple aspects of a single
#object. Like, say, a movie. Define a dictionary called movie that works
#with the following code.
#print "My favorite movie is", movie['title'], "which was released in",
#movie['year'], "and was directed by", movie['director']

movie = {"title": "Julia Roberts and Her Smelly Wig", "year": "2007", "director":
"Kim Kardash", "budget": "10000", "revenue": "500"}
print("My favourite movie is", movie["title"], "which was released in", movie["year"],
"and was directed by", movie["director"],)

#9) Add entries to the movie dictionary for budget and revenue (you'll use code
#like movie['budget'] = 1000), and print out the difference between the two.
#If the movie cost more to make than it made in theaters,
#print "It was a flop". If the film's revenue was more than five times
#the amount it cost to make, print "That was a good investment."

profit = int(movie["revenue"]) - int(movie["budget"])
print("The show made", profit, "dollars")
if profit < 0:
    print("It was a flop")
if int(movie["revenue"]) > int(movie["budget"]) * 5:
    print("It was a good investment")

# Sometimes dictionaries are used to describe the same aspects of many different
# objects. Make ONE dictionary that describes the population of the boroughs of
# NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m,
#Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either
#millions or thousands is a good idea)

population = {"Manhattan": 1600000, "Brooklyn": 2600000, "Bronx": 1400000,
"Queens": 2300000, "Staten Island": 470000}

#Display the population of Brooklyn.
print("The population of Brooklyn is", population["Brooklyn"])

#Display the combined population of all five boroughs.

Combined_Population = sum(population.values())
print("The combined population of all five boroughs is", Combined_Population)

#Display what percentage of New York lives in Manhattan
Manhattan_Percentage = population["Manhattan"] / int(Combined_Population) * 100
print(Manhattan_Percentage, "percent of New York lives in Manhattan")
