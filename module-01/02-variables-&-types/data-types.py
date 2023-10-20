nothing = None

string = "Hello my name is Alejandro Bahena"

integer = 31

flt = 31.5

boolean = True

list = [10, 20, 30, 40]

mixed_list = [10, "twenty", 30, "fourty"]

tple = ("python","masters", "2023")

dictionary = {
    "name": "Alejandro",
    "lastname": "Bahena",
    "curse": "Python master 2023"
}

number_range = range(31)

#print variable
print(nothing)
print(string)
print(integer)
print(flt)
print(boolean)
print(list)
print(mixed_list)
print(tple)
print(dictionary)
print(number_range)


#show data type
print(type(nothing))
print(type(string))
print(type(integer))
print(type(flt))
print(type(boolean))
print(type(list))
print(type(mixed_list))
print(type(tple))
print(type(dictionary))
print(type(number_range))


# convert data
text = "Hello there!"
number = 755
# this can't be done, because python can only concatenate str (not "int") to str 
# print(text + " " +number)

# convert int data into a string
number = str(755)
print(text + " " + number)
