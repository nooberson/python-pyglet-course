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
game_version = 2

# programs run 1 line at a time
# from the top of the file to the bottom
# this line will be printed to the screen first
print('Welcome to my awesome game called:')

# followed by the contents of the "game_name" variable
print(game_name)

# lastly the contents of the "game_version"
# Introduce an error by using an unknown variable name
# by capitalised V of version
print(game_Version)

# and replace the last comment about no more lines to run
# with this line to create a game window
window = pyglet.window.Window()

# and this line to run the game
# now the program won't exit automatically when running out of lines
# the pyglet game window needs to be closed first
pyglet.app.run()

# pyglet is now running
