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

make_shirt(14,'EELTANIM')