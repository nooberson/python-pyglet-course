# lines beginning with a "#" are comments
# comments help us document our code
# but do nothing when the program runs

# we are using the Python programming language
# and the pyglet gaming module
# which we need to import into our program
import pyglet

# let's give our game a name
# and store it in a  variable called "game_name"
# it's called a variable because the value can "vary"
game_name = 'Maze Explorer'

# variables can store numbers, text (strings), dates
# and more complex types like files or a game window
# this is the first version of our game
# let's store that number in a variable too
game_version = 1

# programs run 1 line at a time
# from the top of the file to the bottom
# this line will be printed to the screen first
print('Welcome to my awesome game called:')

# followed by the contents of the "game_name" variable
print(game_name)

# lastly the contents of the "game_version"
print(game_version)

# there are no more lines to run so the program will end
