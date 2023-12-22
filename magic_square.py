#apply a variety of checks to the potential magic square
#return a boolean to indicate its status and the reason for not being a magic square, if applicable
def is_magic_square(potentialMagicSquare):
    #initialize variables
    resultsOfCheck = (True, "")
    numOfRows = 0
    uniqueElements = []
    alreadySeen = False
    #start looping through the square
    for row in potentialMagicSquare:
        numOfRows += 1 #use to track magic square size since it isn't passed as a parameter
        for element in row:
            #check whether all values are in the range of 1 <= x
            if (element < 1):
                stringToReturn = "Invalid or duplicate number was detected"
                resultsOfCheck = (False, stringToReturn)
                return resultsOfCheck
            #check whether the element is a duplicate
            for item in uniqueElements:
                if (item == element):
                    alreadySeen = True
                    stringToReturn = "Invalid or duplicate number was detected"
                    resultsOfCheck = (False, stringToReturn)
                    return resultsOfCheck
            if (not alreadySeen):
                uniqueElements.append(element)

    #initialize some ore variables
    rowSum = [0 for x in range (numOfRows)]
    columnSum = [0 for x in range (numOfRows)]
    rowCount = 0
    
    for row in potentialMagicSquare:
        columnNum = 0
        for element in row:
            #check whether all values are in the range of x <= N^2
            if (element > (numOfRows**2)):
                stringToReturn = "Invalid or duplicate number was detected"
                resultsOfCheck = (False, stringToReturn)
                return resultsOfCheck
            #add the current element to the row and column sums
            rowSum[rowCount] = rowSum[rowCount] + element
            columnSum[columnNum] = columnSum[columnNum] + element
            columnNum += 1
        rowCount += 1

    sumOfAllRows = 0
    #determine whether all items in the row are equal
    #if they are, their total sum should be equal to the product of the first item times the number of rows/columns
    for item in rowSum:
        sumOfAllRows += item
    if (sumOfAllRows != (rowSum[0]*numOfRows)):
        stringToReturn = "A row sum is incorrect"
        resultsOfCheck = (False, stringToReturn)
        return resultsOfCheck

    sumOfAllCols = 0
    #determine whether all items in the column are equal
    #if they are, their total sum should be equal to the product of the first item times the number of rows/columns
    for item in columnSum:
        sumOfAllCols += item
    if (sumOfAllCols != (columnSum[0]*numOfRows)):
        stringToReturn = "A column sum is incorrect"
        resultsOfCheck = (False, stringToReturn)
        return resultsOfCheck
            
    #determine whether the main diagonal is correct
    mainDiagSum = 0
    i = 0
    while (i < numOfRows):
        mainDiagSum += potentialMagicSquare[i][i]
        i += 1
    #determine whether the main diagonal sum is equal to all row/column sums (assumed as equivalent after passing previous checks)
    #if they are, the sum of all rows should be equal to the product of the main diagonal sum times the number of rows/columns
    if (sumOfAllRows != (mainDiagSum*numOfRows)):
        stringToReturn = "Main diagonal sum is incorrect"
        resultsOfCheck = (False, stringToReturn)
        return resultsOfCheck

    #determine whether the main diagonal is correct
    antiDiagSum = 0
    i = numOfRows - 1
    j = 0
    while (j < numOfRows):
        antiDiagSum += potentialMagicSquare[i][j]
        i -= 1
        j += 1
    #determine whether the main diagonal sum is equal to all row/column sums (assumed as equivalent after passing previous checks)
    #if they are, the sum of all rows should be equal to the product of the anti-diagonal sum times the number of rows/columns
    if (sumOfAllRows != (antiDiagSum*numOfRows)):
        stringToReturn = "Anti-diagonal sum is incorrect"
        resultsOfCheck = (False, stringToReturn)
        return resultsOfCheck

    return resultsOfCheck



#read in the file and create a list of lines
inputFile = open("magic.txt", "r")
outputFile = open("results.txt", "w")
listOfLines = inputFile.readlines()
#begin looping through the file's lines
inSquare = False
lineCount = 0
for line in listOfLines:
    #check whether the line is empty
    if (line != "" and line != "\n"):
        #remove extra spaces
        line = line.strip()
        print (line)
        #check whether you are already in a square
        #if not, read in the size of a square
        if (not (inSquare)):
            squareSize = int(line)
            potentialMagicSquare = [[0 for x in range(squareSize)] for y in range(squareSize)]
            inSquare = True
        #if so, read in the square
        elif (inSquare):
            #separate the entities in the line and add them to the array
            words = line.split()
            wordCount = 0
            for word in words:
                word = word.strip()
                potentialMagicSquare[lineCount][wordCount] = int(word)
                wordCount += 1
            lineCount += 1
            #if the file has read in enough lines, reset the flag
            if (lineCount >= squareSize):
                results = is_magic_square(potentialMagicSquare)
                for row in potentialMagicSquare:
                    for element in row:
                        outputFile.write(str(element) + " ")
                    outputFile.write("\n")
                if (results[0]):
                    outputFile.write("MAGIC\n\n")
                    print("MAGIC")
                else:
                    outputFile.write("NOT MAGIC: "+ results[1] + "\n\n")
                    print("NOT MAGIC: "+ results[1])
                inSquare = False
                lineCount = 0
                squareSize = 0