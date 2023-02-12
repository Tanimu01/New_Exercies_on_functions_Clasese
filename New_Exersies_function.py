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