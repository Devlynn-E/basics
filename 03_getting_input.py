# ask the user for their name
username = input("what is your name? ")

# ask the user for their favourite integer
fav_num = int(input("Favourite Number? "))

# double, halve and square the number
double = fav_num * 2
half = fav_num / 2
squared = fav_num * fav_num

# greet the user
print("ello {}, your favourite number is {}".format(username, fav_num))

# output the results of Doubling, Halving
print("here is your number doubled: {}".format(double))
print("and here it is halved: {}".format(half))
print("lastly here it is squared: {}".format(squared))
print()

# and squaring their favourite number.
