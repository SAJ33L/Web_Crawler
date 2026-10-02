"""
This is a simple program that demonstrates the use of the print function in Pythonw
"""
print(3)
print(1+1)
print(3*4)
print(10/2)
print(52*3 + 12*9)
print((52*3)+(12*9))
print(52*(3+12)*9)

"""
Number of minuutes in a week
"""
print(7*24*60)

"""
Using variables
"""
speed_of_light = 299792458
print(speed_of_light*100)

"""
Quiz 
Write Python code to print out how far light travels in a year. 

"""
print(speed_of_light*365*24*60*60)

# use of operators on variables
days = 7*7
days = 48
days = days-1
days = days+1

minutes = 59
minutes = minutes + 1
seconds = minutes * 60
print(seconds)

""""
Quiz
Write Python code that defines the variable age to be your age in years, and then prints out the
number of days you have been alive. If you don't want to use your real age, feel free to use your
age in spirit instead.
"""
age = 25
days_per_year = 365
days_alive = age*days_per_year
print(days_alive)

"""
Quiz
Define a variable, name, and assign to it a string that is your name.
"""
name = "Sajeel"
print(name)

print('My name is ' + name)
print("Hello " + name + "!" + "!")
print("!"*12)
print("BSCSMorning"[4])
print(name[3])
print(name[1:4])

"""
Quiz
Write Python code that prints out Udacity (with a capital U), given the definition
s = 'audacity'
"""
s='audacity'
print(s[0]+s[1].upper()+s[2:])

pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the spheres.'
print(pythagoras.find("string"))
print(pythagoras[40:])
print(pythagoras.find("T"))
print(pythagoras.find("sphere"))
print(pythagoras.find("algebra"))

motto = "We can do programming, yes I can, yes you can."
print(motto.find('can'))
print(motto.find('can', 0))
print(motto.find('can', 3))
print(motto.find('can', 4))
print(motto.find('can', 29))
print(motto.find('can', 30))
print(motto.find('can', 43))

"""
Reading text files
"""
text_file = open('xkcd.txt','r')
print(text_file.readline(5))