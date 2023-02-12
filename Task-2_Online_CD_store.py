#Assignment-2
#Name: Md Asif Iqbal
#Student ID: 29789109
#Task-2 :a program for an on-line CD store (CD_Store.txt)

fileName = open(input("Enter a file name: "))
fileToRead = fileName.read()

def createDatabase(fileToRead):
    """
        createDatabase is a function that creates the database
        by reading from the file CD Store.txt.
        Each line in the file is a comma-separated
        record containing the Title, Artist, Genre and Price of a CD.
        The database is stored as a list of lists.
    """
    record = fileToRead.split('\n')
    final_list = []
    for line in record:
        #Converts the line into strings and puts it in the list
        final_list.append(line.split(','))
    for i in range(len(final_list)):
        """Converts the numbers which are at the end of the row into float
        and puts it in the list"""
        final_list[i][3] = float(final_list[i][3])
    
    return final_list


def displayMenu():
    """
    Program displays a menu with the following options:
    1. Print List of CDs
    2. Sort CDs by Title
    3. Sort CDs by Artist
    4. Sort CDs by Genre
    5. Sort CDs by Price
    6. Find All CDs by Title
    8. Find All CDs by Genre
    9. Find All CDs with Price at Most X.
    10. Quit
    """
    print("1. List of CDs")
    print("2. Sort CDs by Title")
    print("3. Sort CDs by Artist")
    print("4. Sort CDs by Genre")
    print("5. Sort CDs by Price")
    print("6. Find All CDs by Title")
    print("7. Find All CDs by Artist")
    print("8. Find All CDs by Genre")
    print("9. Find All CDs with Price at Most X.")
    print("10. Quit")

def printList(record):
    """
    Program prints the list of CDs in a format that is readable for users
    and includes a identifier what each field is
    """
    for line in range(len(record)):
        string="Title: {0}, Artist: {1}, Genre: {2}, Price: ${3}".format(record[line][0], record[line][1], record[line][2], record[line][3])
        print('\n'+string)
    print()

def sortByTitle(record):
    """
    Updates the list of CDs so that elements are sorted
    in ascending order by title.
    """
    #record is a list that being sorted according to Titles
    for index in range(len(record)-1):
        minPos = index
        for current in range(index+1,len(record)): # Find minimum index
            if record[current][0] < record[minPos][0]:
                minPos = current # Update new minimum index
        record[minPos],record[index] = record[index],record[minPos] # Swap
    printList(record)
    return record

def sortByGenre(record):
    """
    Updates list of CDs so that elements are sorted in ascending order by genre.
    """
    for index in range(len(record)-1):
        minPos = index
        for current in range(index+1,len(record)):   # Find minimum index
            if record[current][2] < record[minPos][2]:
                minPos = current    # Update new minimum index
        record[minPos],record[index] = record[index],record[minPos] # Swap
    printList(record)

def sortByArtist(record):
    """
    Updates the list of CDs so that elements are sorted in ascending order
    by artist.
    """
    for index in range(len(record)-1):  #So that it doesn't go outside the list.
        minPos = index              #This assigns minPos to the index of the list.
        for current in range(index+1,len(record)): # Find minimum index
            if record[current][1] < record[minPos][1]:
                minPos = current # Update new minimum index
        record[minPos],record[index] = record[index],record[minPos] # Swap
    printList(record)

def sortByPrice(record):
    """
    Program sorts the list of CDs by the price attribute.
    """
    for index in range(len(record)-1):
        minPos = index
        for current in range(index+1,len(record)): # Find minimum index
            if float(record[current][3]) < float(record[minPos][3]):
                minPos = current # Update new minimum index
        record[minPos],record[index] = record[index],record[minPos] # Swap

    printList(record)

def findByTitle(cdList):
    """
    Program prints all elements in the list of CDs that
    have a title that matches target.
    """
    target = input("Enter a Title: ").lower()
    position = 0
    fList=[]                    #fList is an empty list
    while position < len(cdList):
        title = cdList[position][0].lower()
        #Checks if the input is contained within the rows' artist
        if target in title:
            fList.append(cdList[position])
        position += 1
    printList(fList)

def findByArtist(cdList):
    """
    Program prints all elements in the list of CDs that have
    the genre given in target.
    """
    target = input("Enter an Artist: ").lower()
    position = 0
    fList=[]                             #fList is an empty list
    while position < len(cdList):
        artist = cdList[position][1].lower()
        #Checks if the input is contained within the rows' artist
        if target in artist:
            fList.append(cdList[position])
        position += 1
    printList(fList)

def findByGenre(cdList):
    """
    Program prints all elements in the list of CDs that have
    the artist that matches target.
    """
    target = input("Enter a Genre: ").lower()
    position = 0
    fList=[]
    while position < len(cdList):
        genre = cdList[position][2].lower()
        #Checks if the input is contained within the rows' artist
        if target in genre:
            fList.append(cdList[position])
        position += 1
    printList(fList)

def findByPrice(intList):
    """
    Program finds all CDs that cost at most the amount specified by price.
    """
    target = inputCheck()
    position = 0
    fList=[]
    while position < len(intList):
        #This gives me everything that is less than or equal to the target.
        if float(intList[position][3]) <= float(target):   
            fList.append(intList[position])
        position += 1
    printList(fList)

def inputCheck():
    """
    inputCheck is the function that checks if it is a
    valid input or not
    """
    #To make sure that the user is inputting floats only.
    while True:
        try:
            return float(input("Enter the Price: "))
        except:
            print("That's not a valid input!! Enter a number.")

#database is the variable that calls createDatabase() function.
database = createDatabase(fileToRead)  
#displayMenu()

def main():
    """
    Takes the user input and checks if it is valid or not
    and also calls the function DisplayMenu
    """
    flag = True
    while flag:
        displayMenu()
        select = input("Enter a number: ")
        if select == '1':
            printList(database)
        elif select == '2':
            sortByTitle(database)
        elif select == '3':
            sortByArtist(database)
        elif select == '4':
            sortByGenre(database)
        elif select == '5':
            sortByPrice(database)
        elif select == '6':
            findByTitle(database)
        elif select == '7':
            findByArtist(database)
        elif select == '8':
            findByGenre(database)
        elif select == '9':
            findByPrice(database)
        elif select == '10':
            flag = False
        else:
            print("invalid")

main()
fileName.close()
