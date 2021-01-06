place = input("Enter a place: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective3 = input("Enter an adjective: ")
number = input("Enter a number: ")
adjective4 = input("Enter an adjective: ")
colour = input("Enter a colour: ")
adjective5 = input("Enter an adjective: ")


print(f'''My home is located in {place}. I live in a {adjective1} row house, which flaunts a {adjective2} yet dainty {noun} at the entrance to my home. As you enter you will see an elegant formal living room attached to which is our {adjective2} family dining room. Adjacent to our munching area is a {adjective3} kitchen that is a fashionable open one. We have {number} graceful and fancy bedrooms with the master bath on one side There are {adjective4} curtains running throughout the house and the entire house is painted in a {colour} tint bringing in the required {adjective5} and airiness.''', file = open("output.txt", "w"))