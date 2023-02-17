# Try It Yourself
# 8-1. Message: Write a function called display_message() that prints one sentence
#telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.
def display_message():
    print('I am learning how to use finctions')

display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
#parameter, title. The function should print a message, such as One of my
#favorite books is Alice in Wonderland. Call the function, making sure to
#include a book title as an argument in the function call.

def favorite_book(book_title):
    print('favorite books is Alice in', book_title)

favorite_book('Wonderland')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def  make_shirt(size,text):
    print('this is my size: ' , size,' and the text to be printed is',text)

make_shirt('Medium','EELTANIM')
make_shirt(size='Medium',text='EELTANIM')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different message.
def  make_shirt(text, size='large',):
      print('this is my size: ' , size,' ',text)
make_shirt('I love python')

def  make_shirt(size,text='I love python'):
      print('this is my size: ' , size,' ',text)
make_shirt('Medium')
make_shirt('small','I am happy for learning function')

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

def describe_city(city, country='Nigeria'):
    print(city, ' is in ', country)

describe_city('kano')
describe_city('Sule Tankarkar')
describe_city(city='Zandar',country='Niger')

# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"

def city_country(country, city):
	countrycity=country, city
	return countrycity
print(city_country('santiago', 'chile'))
print(city_country('Nigeria', ' Kano'))
print(city_country('Niger', 'zandar'))

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album


def make_album(artist_name, album_title):
  album_detail={'artist': artist_name, 'album':album_title}
  
  return album_detail
print(make_album('Nura M Inuwa', 'Soyayya Ruwan Zuma'))
print(make_album('Haruna Oji', 'Balaraba'))
print(make_album('Style Plus', 'Four years no waka'))
print(make_album('Style Plus', 'Four years no waka'))

def make_album(artist_name, album_title, no_songs=None):
  album_detail={'artist': artist_name, 'album':album_title}
  if no_songs:
    album_detail[no_songs] = no_songs 

  return album_detail
print(make_album('Nura M Inuwa', 'Soyayya Ruwan Zuma'))
print(make_album('Haruna Oji', 'Balaraba',4))
print(make_album('Style Plus', 'Four years no waka',3))
print(make_album('Style Plus', 'Four years no waka',5))


#8-8. User Albums: Start with your program from Exercise 8-7. Write a while
#loop that allows users to enter an album’s artist and title. Once you have that
#information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.


def make_album(artist_name, album_title):
  album_detail={'artist': artist_name, 'album':album_title}
  
  return album_detail

while True:
    print('enter q to quit anytime')
    artname=input('enter artist name')
    if artname=='q':
        break
    print('enter q to quit anytime')
    albtle=input('enter album title')
    if albtle=='q':
        break
    print(make_album(artname,albtle))

# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.

def show_messages(family_name):
    for family in family_name:
        print('You are welcome my family memebr  :', family)
family_list=['Tanimu','Amina', 'Saadatu','Aisha','Shamsu', 'Sadiq']
show_messages(family_list)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were moved correctly.

def show_messages(family_name):
    for family in family_name:
        print('You are welcome my family memebr  :', family)
def send_messages(family_name, new_list):
  while family_name:
    current_list=family_name.pop()
    print('the current list is ', current_list)
    new_list.append(current_list)

family_list=['Tanimu','Amina', 'Saadatu','Aisha','Shamsu', 'Sadiq']
new_list=[]
show_messages(family_list)
send_messages(family_list,new_list)
print(new_list)
print(family_list)

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its messages.

def show_messages(family_name):
    for family in family_name:
        print('You are welcome my family memebr  :', family)
def send_messages(family_name, new_list):
  while family_name:
    current_list=family_name.pop()
    print('the current list is ', current_list)
    new_list.append(current_list)

family_list=['Tanimu','Amina', 'Saadatu','Aisha','Shamsu', 'Sadiq']
new_list=[]
show_messages(family_list)
send_messages(family_list[:],new_list)
print(new_list)
print(family_list)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that’s being ordered. Call the function three times, using a different number of arguments each time.


def person_need(*sandwichs):

 print('you like : ')
 for sanwich in sandwichs:
  print(f"- {sanwich}")
person_need('egg')
person_need('egg', 'flour', 'suger')
person_need('water', 'butter','suger','egg')

# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
# profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
 user_info['first_name'] = first
 user_info['last_name'] = last
 return user_info
user_profile = build_profile('Tanimu', 'Abdullahi',
location='Kano',
field='Computer science', sex='Male')
print(user_profile)

# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)

def car_information(manufacturer, model_name, **other_information):
  other_information['Manufac'] = manufacturer
  other_information['model'] = model_name
  return other_information

print(car_information('Honda','2007',color='red',glass='typing'))
 
 # 8-15. Printing Models: Put the functions for the example printing_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of printing_models.py, and modify the file to use the imported functions.


# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import addition_function
print(addition_function.addition(5,9))
from addition_function import addition
print(addition(2,3))
from addition_function import addition as fn
print(fn(1,1))
import addition_function as mn
print(mn.addition(0,1))
from addition_function import*
print(addition(1,9))
