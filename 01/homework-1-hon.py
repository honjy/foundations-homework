#Jing Yi Hon
#May 23, 2016
#Homework 1
name = input("What, Good Sir, is your name?")
print("I bid thee good day " + name)

year_of_birth = input("What year were you born in?")
if int(year_of_birth) > 2016:
    year_of_birth = input("Are you sure? Try again")
    age = 2016 - int(year_of_birth)
    print("You are", age, "years old.")
else:
    age = 2016 - int(year_of_birth)
    print("You are", age, "years old.")

#Assuming average heart rate is 72bmp because I can't be bothered to count
#based on average heart rate of an infant + teenager + adult
#Heartbeats a year = 72 x 60 x 24 x 365 = 37843200
heartbeats = 37843200 * int(age)
print("Congratulations, your heart has beat a total of", heartbeats, "times.")
print("That's pretty amazing.")

#A blue whale's heart only beats six times a minute!
bluewhale = 3153600 * int(age)
print("And if you were a whale, your heart would only have beat", bluewhale, "times.")

#Assuming a rabbit's heart beats 130 times a minute.
rabbit = 68328000 * int(age)
rabbitbil = int(rabbit) / 1000000000
if rabbit > 1000000000:
    print("But if you were a bunny, your heart would have beat", rabbitbil, "billion times by now.")
else:
    print("But if you were a bunny, your heart would have beat", rabbit, "times by now.")

#A year on Earth equates to 224 days on Venus
venus = int(age) * 365 / 224
print("If you lived on Venus, you would be", venus, "years old.")

#A year on Earth equates to 165 years on Neptune
neptune = int(age) / 165
print("But if you lived on Neptune, you would be", neptune, "years old.")

#I am 28, fyi
if age == 28:
    print("Hey you're hot and we're the same age.")
elif age < 28:
    print("You're an arse and you're younger than I am.")
    youngage = 28 - int(age)
    print("You are", youngage, "years younger than I am. Buy yourself a cake.")
else:
    print("HA you are old.")
    oldage = int(age) - 28
    print("You are", oldage, "years older than I am. You can buy me a cake.")

#Whether they were born in an even or odd year

if int(year_of_birth) % 2 == 0:
    print("Congratulations, you were born in an even year, though I am not sure why it matters")
else:
    print("You were born in an odd year, like the oddball you are.")

#Superbowl, urgh
if int(year_of_birth) > 2008:
    print("The Pittsburg Steelers have never won the Superbowl while you were alive.")
elif int(year_of_birth) > 2006:
    print("The Pittsburg Steelers have won the Superbowl once since you've been born.")
elif int(year_of_birth) >= 1980:
    print("The Pittsburg Steelers have won the Superbowl twice since you've been born.")
elif int(year_of_birth) >= 1979:
    print("The Pittsburg Steelers have won the Superbowl thrice since you've been born.")
elif int(year_of_birth) >= 1978:
    print("The Pittsburg Steelers have won the Superbowl four times since you've been born.")
elif int(year_of_birth) >= 1975:
    print("The Pittsburg Steelers have won the Superbowl five times since you've been born.")
else:
    print("The Pittsburg Steelers have won the Superbowl six times since you were born.")

if int(year_of_birth) >= 2009:
    print("President Obama was in office when you were born.")
elif int(year_of_birth) >= 2001:
    print("President Bush was in office when you were born.")
elif int(year_of_birth) >= 1993:
    print("President Clinton was in office when you were born.")
elif int(year_of_birth) >= 1989:
    print("President Bush was in office when you were born.")
elif int(year_of_birth) >= 1981:
    print("President Reagan was in office when you were born.")
elif int(year_of_birth) >= 1974:
    print("President Ford was in office when you were born.")
elif int(year_of_birth) >= 1969:
    print("President Nixon was in office when you were born.")
elif int(year_of_birth) >= 1961:
    print("President Kennedy was in office when you were born.")
elif int(year_of_birth) >= 1953:
    print("President Eisenhower was in office when you were born.")
elif int(year_of_birth) >= 1945:
    print("President Truman was in office when you were born.")
elif int(year_of_birth) >= 1933:
    print("President FDR was in office when you were born.")
else:
    print("You are too old and I don't have to calculate which President was in office when you were born.")
