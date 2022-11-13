#-------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Dfredin, 2022-Nov-11, Modified file to use dictionaries and loading/deleting functionality
#-------------------------------------------#
# Declare variables
menuChoice = '' # User input
intInput = int() #User input for deletion
lstTbl = []  # list of lists to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
flag = bool()
import os.path
# ---------- PRESENTATION (I/O) ----------- #
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    menuChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    if menuChoice == 'x':
        break # 5. Exit the program if the user chooses to
# -------------- PROCESSING --------------- #  
    if menuChoice == 'l':
        flag = os.path.isfile(strFileName) # Testing to see if file exists
        if flag:
            lstTbl.clear() # Clears the table so as to not duplicate data before loading
            objFile = open(strFileName, 'r')
            for row in objFile:
                lstRow = row.strip().split(',')
                dicRow = {'id': int(lstRow[0]), 'title': lstRow[1], 'artist': lstRow[2]}
                lstTbl.append(dicRow)
            objFile.close() 
        else:
            print('The file does not exist. Add CDs first.\n')
# ---------- PRESENTATION (I/O) ----------- #
    elif menuChoice == 'a':
        # 2. Add data to the table (2d-list) each time the user wants to add data
        # TODO Wanted to add a check to see if added CD is already in inventory before duplicating
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        # TODO Want to add an error message when user inputs anything but an Integer
        dicRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)  
    elif menuChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        if len(lstTbl) == 0: # Checks if the list of dicts is empty before  
            print('Please load the Inventory from file before displaying!\n') # If empty then asks to load
        else:
            print('========CD INVENTORY========') # If data has been loaded, then displays it
            print('ID, CD Title, Artist') 
            for row in lstTbl:
                print(*row.values(), sep = ', ')
            print() # Leaves an empty line after displaying Inventory
# -------------- PROCESSING --------------- #         
    elif menuChoice == 'd':
        if len(lstTbl) == 0: # Checks if the list of dicts is empty before  
            print('Please load the Inventory from file before deleting!\n') # If empty then asks to load
        else:
            print('====CURRENT CD INVENTORY====') # Gives current inventory for user to choose from to delete
            print('ID, CD Title, Artist') 
            for row in lstTbl:
                print(*row.values(), sep = ', ')
            print() 
            intInput = int(input('What ID would you like to delete? ')) # Takes user input for deletion
            for i in range(len(lstTbl)):
                if lstTbl[i]['id'] == intInput:
                    print('You have deleted the following CD: \n',
                          str(lstTbl[i]['id']),',', 
                          str(lstTbl[i]['title']),',', 
                          str(lstTbl[i]['artist']))
                    print()
                    del lstTbl[i] # Deletes the entry the user chooses
                    break 
            objFile = open(strFileName, 'w') # Writes new inventory into new file, overwriting old file
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()
            lstTbl.clear() # Clears table to user doesn't continue added same CD to inventory
# -------------- PROCESSING --------------- #
    elif menuChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        if len(lstTbl) == 0: # Checks if the list of dicts is empty before  
            print('Please add to the Inventory before saving!\n') # If empty then asks to load
        else:
            objFile = open(strFileName, 'a')
            for row in lstTbl:
                strRow = ''
                for item in row.values():
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
                objFile.write(strRow)
            objFile.close()
            lstTbl.clear() # Clears table to user doesn't continue added same CD to inventory
    else:
        print('Please choose either l, a, i, d, s or x!\n')        
print('Good bye!') # Exit statement