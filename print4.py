# More printing

type_of_people = 100 
X = f"There are {type_of_people} types of people"

Binary = "Binary"
do_not = "don't"

Y = f"Those who know {Binary} and those who {do_not}."
                                             
print(X)
print(Y)

print(f"I said : {X}.") 
print(f"I also said : '{Y}'")

hilarious = True
joke_evaluation = "Isn't that joke was funny?! {} "
                                             
print(joke_evaluation.format(hilarious))                                             
                                             
w = "This is the left side of... "                                             
e = " a string with the right side"

print(w+e)                                             
