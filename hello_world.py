# 1. TASK: print "Hello World"
print("Hello World")


# 2. print "Hello Jacob!" with the name in a variable
name = "Jacob"
print("Hello " + name)
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +


# 3. print "Hello 42!" with the number in a variable
num = "3"
print("Hello " + str(num))
# print( your code here )	# with a comma
print("Hello", str(num))
# print( your code here )	# with a +	-- this one should give us an error!
print("Hello " + str(num))


# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "yum yums"
fave_food2 = "snackeronis"
print("I love to eat " + fave_food1 + " and " + fave_food2)
# print( your code here ) # with .format()
print("I love to eat {} and {}.".format(fave_food1, fave_food2))
# print( your code here ) # with an f string
print(f"I love to eat {fave_food1} and {fave_food2}.")

