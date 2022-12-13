# Video Game Image Guessing Game
    #### Video Demo:  https://youtu.be/nv0Met9iA2c
    #### Description:

    # Preface
    ### My inital idea was to make a trivia game, I wanted to grab a question, ask for an answer & then compare & display weather the question was answered correctly. Continuing my planning this evolved into a video game guessing game, but I wanted to do something more graphical & engaging instead of just using the terminal to show & answer the questions. Searching around I found a video game API called RAWG, they have thousands of games' information including pictures, the name, relase date & more, this was what I ultemately decided to use. I then decided to use tkinter to create a simple GUI for making your guess.

    # Getting Started
    ### My first task was calling, pulling & saving the name of a random video game to compare against the player's answer & the image associated with the game in the API's data. For this I used the random library to randomly generate a number for the page parameter in my request URL & the requests library to call to the API & grab a JSON response, this allowed me to easily save the 2 pieces of data I needed to create the game. To do so I parsed the response by the keys inside the dictionary object coming from the API 'name' & 'background_image' respectively.

    # Saving The Dictionary Info
    ### After calling the API, getting data & parsing the pieces of information I need I decided to save this information to a csv, making it easier to reference for the later part of the program. The API returned to me the name of the video game as a string & also an image URL pointing to to the image that is saved for the game in their database. Since the object returned is a dictionary I used csv.DictReader() to save the information to a csv file with the keys of name & image so I can continue to refence this information with associated keys.

    # Creating Game Window & Playing
    ### The longest part of the program was creating the GUI with the tkinter package with python. This package allows for the easy creation of simple GUI interfaces using only python. I first started by creating the main window, this is used as the reference to all other tkinter functions. The next step was to grab the picture to display from the URL that is saved to the csv on the request to the API. To do this I needed to open the photo from the URL, I did this using urolopen() from the urllib3 library by importing the function from urllib3.requests.

    After opening the URL containing the image, I used Image.open() from the pillow python library to open the image as an object I can use for display. I then created a separate function to resize the image to an apropriate size so that the photo isn't wildly out of proportion or to large for the window. Using the ImageTk class from the pillow library (This is a special class created by pillow to work with tkinter) I took the resized image & created a final variable named 'photo' with the image to be used on the window & an image area so tkinter knows how to place the picture.

    The final process in this function is starting the mainloop & displaying the window with all the information (picture, entry field & button). Using tkinter I created an entry field for the user to enter their answer & a button for the user to submit their answer. Inside the funtion that creates & displays the window, I created a function, named click, that actives when the submit button is pressed. This function removes everything currently displayed on the screen, compares your inputted answer to the correct answer in the csv & either shows 'correct' if you answered correct, or what the correct answer is.

    # Conclusion
    ### Using these python libraries I created a video game guessing game using a photo as the clue. I used the RAWG API to retieve the information with the requests library & parsed that information for use with tkinter, which is how the game is played through entering in your answer & pressing the submit button.