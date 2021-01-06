noun1 = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
noun2 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter a verb: ")
noun3 = input("Enter a noun: ")
colour = input("Enter a colour: ")
name = input("Enter your name: ")

print(f'''\nA happy Child :

My {noun1} is {adjective1} - a {adjective1} {noun1};
A {adjective2} {noun2} am I:
I laugh and {verb1} the whole day long,
I hardly ever {verb2}.

I have a {noun3}, a {colour}, {colour} {noun3},
To shade me from the sun;
And under it I often sit,
When all my {verb1} is done.

By {name}\n\n''', file = open("output.txt", "w"))