# magic-squares
This program reads in a series of squares from a text file called magic.txt. The first line will indicate the square's size with the following lines being the square. The file's input is stored in a two-dimensional array for later analysis.
The array of data is passed to a function which evaluates it to determine whether it is a valid magic square. This function returns a boolean to indicate the square's status and the reason for not being a magic square, if applicable.
Those results, as well as their associated squares are finally printed out in a file called results.txt.