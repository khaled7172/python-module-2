*This project has been created as part of the 42 curriculum by khhammou*

## Description

raise is how python signals something went wrong
you throw an error when your program detects a problem
example if a plant is wilting
raise PlantError("The tomato plant is wilting!")
Raising an exception stop flow of program adn jumps to error handling
except/catching
catching is handling the error so the program doesnt crash
you can use a try block to wrap code that might raise an error
you use except to catch that error and respond like printing a message or doing a fix
example:
trying to water a plant and water tank is empty
raise WaterError("empty tank!")
catch it print "caught waterError: empty tank!" so program continues
example flow
code runs inside try
something goes wrong
raise triggers an error
python jumps to except block
code in except executes so program doesnt crash
optionally finally can run code that must happen no matter what

Exceptions
python has built in exceptions
to crete your own exception, create a class that inherits from Exception built in
inheritance is:
child gets all behavior of parent, but can be customized
catch all garden-related errors by catching the parent(GardenError)
instead of writing seperate except blocks for each child
catching GardenError also catches PlantError and WaterError


Go crazy:
autopep8 --in-place --aggressive --aggressive ft_garden_management.py
### Instructions

You run this code by doing python3 file_name.py

## Resources

The internet

## AI Usage

Testing my code with test cases and helping me find syntax errors