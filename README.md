# instdep
simple python program for installing requirements/dependencies for python

# usage

make a text file:

use '=' to mark command for following packages 

use '+' to mark arguments for packages

list packages

run: "python instdep.py [text file]" 

# example of the text file

    =git
    +clone
    https://github.com/ismotee/instdep.git

    =pip
    +install
    pockets
    black
