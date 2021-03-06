
import ast
import sqlite3
import os


# Example of a function/subroutine
def main():
    print("")
    print("Would you like to:") # Example of a string
    print("a) Sign in")
    print("b) Sign up")
    print("c) End program")
    answer = input("> ") # Example of a (local) variable and assignment

    # Example of an if else statement/selection
    if (answer == "a"):
        login()
        
    elif (answer == "b"):
        register()

    elif (answer == "c"):
        pass

    elif (answer == "x"):
        # Example of variable declaration and a global variable
        global userLogin
        userLogin = "jigglyJ"
        songMain()
        
    else:
        print("Invalid input.")
        main()


def register():
    userList = open("users.txt","r").read()
    userList = ast.literal_eval(userList)


    print("")
    print("Please enter your details below.")
    print("If you would like to exit the sign up process at any time,")
    print("simply type \'exit\' at any time.")

    
    
    def registerName():
        

        def registerUser():


            def registerEmail():
                

                def registerPassword():

  
                    def registerAdd():
                        userList[0].append(newName)
                        userList[1].append(newUser)
                        userList[2].append(newEmail)
                        userList[3].append(newPassword)

                        # Example of writing to a text file
                        userAdd = open("users.txt","w")
                        userAdd.write(str(userList))
                        userAdd.close()


                        print("Account successfully created.")
                        print("Returning to main menu.")


                        main()

                        #registerAdd end


                    print("")
                    newPassword = input("Please enter your password here:")

                    for character in newPassword:
                        if character not in verifyArray:
                            print("Invalid input.")
                            registerPassword()

                    if (newPassword == "exit"):
                        main()

                    else:
                        print("")
                        newPasswordVerify = input("Please re-enter your password here:")

                        if (newPasswordVerify == "exit"):
                            main()

                        elif (newPasswordVerify == newPassword):
                            registerAdd()

                        else:
                            print("Passwords do not match.")
                            print("Please re-enter password.")
                            registerPassword()

                        
                    #registerPassword end


                print("")
                newEmail = input("Please enter your e-mail here:")

                for character in newEmail:
                    if character not in verifyArray:
                        print("Invalid input.")
                        registerEmail()
                
                
                if (newEmail == "exit"):
                    main()

                elif ("@" in newEmail and "." in newEmail and " " not in newEmail and newEmail.count("@") == 1):
                        registerPassword() 

                else:
                    print("Invalid E-mail.")
                    registerEmail()
                    
                
                #registerEmail end


            print("")
            newUser = input("Please enter your username here:")

            for character in newUser:
                if character not in verifyArray:
                    print("Invalid input.")
                    registerUser()
            

            if (newUser == "exit"):
                main()
        
            elif (newUser in userList[1]):
                print("Unfortunately, that username already exists.")
                print("Please try another username.")
                registerUser()

            else:
                registerEmail()

            #registerUser end


        print("")
        newName = input("Please enter your name here:")

        for character in newName:
            if character not in verifyArray:
                print("Invalid input.")
                registerName()
        
        
        if (newName == "exit"):
            main()
            
        else:
            registerUser()

        #registerName end


    registerName()

    #register end


def login():
    # 'users.txt' contains a multi-dimensional array
    userList = open("users.txt","r").read() # Example of reading from a text file
    userList = ast.literal_eval(userList)

    print("")
    print("Please enter your sign in information.")
    global userLogin # Example of a global variable
    userLogin = input("Enter username:")
    passwordLogin = input("Enter Password:")
    if (userLogin in userList[1]):
        userIndex = userList[1].index(userLogin)
        if (userList[3][userIndex] == passwordLogin):
            print("Sign in successfull.")
            print("Welcome, " + userLogin + ".")
            songMain()
            
        else:
            print("The username or password you entered is incorrect, please try again.")
            print("")
            print("Would you like to re-enter your username and password?")
            print("a) Yes")
            print("b) No")
            answer = input("> ")


            if (answer == "a"):
                login()
                
            elif (answer == "b"):
                main()
                
            else:
                print("Invalid entry.")
                print("Returning to main menu.")
                main()
            
        
    else:
        print("The username or password you entered is incorrect, please try again.")
        print("")
        print("Would you like to re-enter your username and password?")
        print(" a) Yes")
        print(" b) No")
        answer = input("> ")


        if (answer == "a"):
            login()
            
        elif (answer == "b"):
            main()
            
        else:
            print("Invalid entry.")
            print("Returning to main menu.")
            main()


def songMain():
    print("")
    print("Would you like to:")
    print("a) List songs")
    print("b) Sort all songs")
    print("c) Create, edit or sort playlists")
    print("d) Search for a song")
    print("e) Edit account details")
    print("f) Sign out")
    answer = input("> ")

    
    if (answer == "a"):
        listSongs()

    elif (answer == "b"):
        sortSongs()

    elif (answer == "c"):
        playlist()

    elif (answer == "d"):
        searchSongs()

    elif (answer == "e"):
        editAccount()

    elif (answer == "f"):
        print("Signing out...")
        print("Returning to main menu.")
        main()

    else:
        print("Invalid input.")
        songMain()


def listSongs():
    print("")
    print("Listing songs:")
    print("")

    cursor.execute('SELECT songName, artistName, genre, album, length FROM songs')

    #Example of for loop/iteration
    for row in cursor:
        print("| Song: ", row[0], end=" | ")
        print("Artist: ", row[1], end=" | ")
        print("Genre: ", row[2], end=" | ")
        print("Album: ", row[3], end=" | ")
        print("Length: ", row[4], " |")

    
    songMain()


def sortSongs():
    
    print("")
    print("Do you want to list songs by:")
    print("a) Name")
    print("b) Artist")
    print("c) Genre")
    print("d) Album")
    print("e) Length")
    answer = input("> ")

    if (answer == "a"):
        print("Do you want to:")
        print("a) Sort from A - Z")
        print("b) Sort from Z - A")
        answer2 = input("> ")
        
        if (answer2 == "a"):
            cursor.execute('SELECT songName, artistName, genre, album, length FROM songs ORDER BY songName ASC')

        elif (answer2 == "b"):
            cursor.execute('SELECT songName, artistName, genre, album, length FROM songs ORDER BY songName DESC')

        else:
            print("Invalid entry.")
            print("Would you like to try again?")
            print(" a) Yes")
            print(" b) No")
            answer = input("> ")

            if (answer == "a"):
                sortSongs()
                    
            elif (answer == "b"):
                songMain()
                    
            else:
                print("Invalid entry.")
                print("Returning to menu.")
                songMain()


        for row in cursor:
            print("| Song: ", row[0], end=" | ")
            print("Artist: ", row[1], end=" | ")
            print("Genre: ", row[2], end=" | ")
            print("Album: ", row[3], end=" | ")
            print("Length: ", row[4], " |")


        # Name sort end


    elif (answer == "b"):
        print("Do you want to:")
        print("a) Sort from A - Z")
        print("b) Sort from Z - A")
        answer2 = input("> ")
        
        if (answer2 == "a"):
            cursor.execute('SELECT songName, artistName, genre, album, length FROM songs ORDER BY artistName, album ASC')
            
        elif (answer2 == "b"):
            cursor.execute('SELECT songName, artistName, genre, album, length FROM songs ORDER BY artistName, album DESC')
            
        else:
            print("Invalid entry.")
            print("Would you like to try again?")
            print(" a) Yes")
            print(" b) No")
            answer = input("> ")

            if (answer == "a"):
                sortSongs()
                    
            elif (answer == "b"):
                songMain()
                    
            else:
                print("Invalid entry.")
                print("Returning to menu.")
                songMain()


        for row in cursor:
            print("| Song: ", row[0], end=" | ")
            print("Artist: ", row[1], end=" | ")
            print("Genre: ", row[2], end=" | ")
            print("Album: ", row[3], end=" | ")
            print("Length: ", row[4], " |")


        # Artist sort end


    elif (answer == "c"):
        print("Do you want to:")
        print("a) Sort from A - Z")
        print("b) Sort from Z - A")
        answer2 = input("> ")
        
        if (answer2 == "a"):
            cursor.execute('SELECT songName, artistName, genre, album, length FROM songs ORDER BY genre, artistName, album ASC')
            
        elif (answer2 == "b"):
            cursor.execute('SELECT songName, artistName, genre, album, length FROM songs ORDER BY genre, artistName, album DESC')
            
        else:
            print("Invalid entry.")
            print("Would you like to try again?")
            print(" a) Yes")
            print(" b) No")
            answer = input("> ")

            if (answer == "a"):
                sortSongs()
                    
            elif (answer == "b"):
                songMain()
                    
            else:
                print("Invalid entry.")
                print("Returning to menu.")
                songMain()


        for row in cursor:
            print("| Song: ", row[0], end=" | ")
            print("Artist: ", row[1], end=" | ")
            print("Genre: ", row[2], end=" | ")
            print("Album: ", row[3], end=" | ")
            print("Length: ", row[4], " |")


        # Genre sort end


    elif (answer == "d"):
        print("Do you want to:")
        print("a) Sort from A - Z")
        print("b) Sort from Z - A")
        answer2 = input("> ")
        
        if (answer2 == "a"):
            cursor.execute('SELECT songName, artistName, genre, album, length FROM songs ORDER BY album ASC')
            
        elif (answer2 == "b"):
            cursor.execute('SELECT songName, artistName, genre, album, length FROM songs ORDER BY album DESC')
            
        else:
            print("Invalid entry.")
            print("Would you like to try again?")
            print(" a) Yes")
            print(" b) No")
            answer = input("> ")

            if (answer == "a"):
                sortSongs()
                    
            elif (answer == "b"):
                songMain()
                    
            else:
                print("Invalid entry.")
                print("Returning to menu.")
                songMain()


        for row in cursor:
            print("| Song: ", row[0], end=" | ")
            print("Artist: ", row[1], end=" | ")
            print("Genre: ", row[2], end=" | ")
            print("Album: ", row[3], end=" | ")
            print("Length: ", row[4], " |")


        # Album sort end

    elif (answer == "e"):
        print("Do you want to:")
        print("a) Sort from low - high")
        print("b) Sort from high - low")
        answer2 = input("> ")
        
        if (answer2 == "a"):
            cursor.execute('SELECT songName, artistName, genre, album, length FROM songs ORDER BY length ASC')
            
        elif (answer2 == "b"):
            cursor.execute('SELECT songName, artistName, genre, album, length FROM songs ORDER BY length DESC')
            
        else:
            print("Invalid entry.")
            print("Would you like to try again?")
            print(" a) Yes")
            print(" b) No")
            answer = input("> ")

            if (answer == "a"):
                sortSongs()
                    
            elif (answer == "b"):
                songMain()
                    
            else:
                print("Invalid entry.")
                print("Returning to menu.")
                songMain()


        for row in cursor:
            print("| Song: ", row[0], end=" | ")
            print("Artist: ", row[1], end=" | ")
            print("Genre: ", row[2], end=" | ")
            print("Album: ", row[3], end=" | ")
            print("Length: ", row[4], " |")


        # Length sort end

    else:
        print("Invalid entry.")
        print("Would you like to try again?")
        print(" a) Yes")
        print(" b) No")
        answer = input("> ")

        if (answer == "a"):
            sortSongs()
                
        elif (answer == "b"):
            songMain()
                
        else:
            print("Invalid entry.")
            print("Returning to menu.")
            songMain()

    
    songMain()


def playlist():
    print("")
    print("Do you want to:")
    print("a) Create a playlist")
    print("b) Edit a playlist")
    print("c) View a playlist")
    print("d) Return to menu")
    answer = input("> ")

    
    if (answer == "a"):
        playlistCreate()
        
    elif (answer == "b"):
        playlistEdit()

    elif (answer == "c"):
        playlistView()

    elif (answer == "d"):
        songMain()
        
    else:
        print("Invalid input.")
        playlist()
    
    
def playlistCreate():
    print("")
    print("WARNING: If you create a playlist with the same name")
    print("as one that already exists, the old one will be overwritten.")
    print("")
    print("Enter playlist name:")
    playlistName = input("> ")

    for character in playlistName:
        if character not in verifyArray:
            print("Invalid input.")
            registerCreate()


    repeat = True # Example of a boolean
    songIndex = 0 # Example of an integer
    playlistAdd = [""] * 25 # Example of an array

    print("")
    print("While adding songs to the playlist")
    print("type \'exit\' at any time to return to the menu")
    print("or type \'finish\' if you have finished entering")
    print("songs into the playlist.")

    # Example of while loop
    while (repeat == True):
        print("")
        print("Input song name (case sensitive):")
        playlistAdd[songIndex] = input("> ")

        if (playlistAdd[songIndex] == "exit"):
            songMain()
            repeat = False

        elif (playlistAdd[songIndex] == 'finish'):
            playlistAdd[songIndex] = ""
            
            repeat = False

        elif (cursor.execute("SELECT songName FROM songs WHERE songName = ?",(playlistAdd[songIndex],)).fetchone()):
            if (songIndex >= 24):
                print("Song limit reached.")
                repeat = False

            else:
                # Example of addition
                songIndex = songIndex + 1

        else:
            print("Invalid song name.")


    if (songIndex < 24):
        songIndex = songIndex - 1

    
    newPlaylist = sqlite3.connect(playlistName + '.db')

    playlistCursor = newPlaylist.cursor()

    playlistCursor.execute('DROP TABLE IF EXISTS songs')

    playlistCursor.execute('CREATE TABLE IF NOT EXISTS songs(id INTEGER PRIMARY KEY, songName TEXT, artistName TEXT, genre TEXT, album TEXT, length TEXT)')

    addIndex = 0

    while (addIndex < songIndex + 1):
        song = playlistAdd[addIndex]
       
        cursor.execute('SELECT songName, artistName, genre, album, length FROM songs WHERE songName = ?', (song,))
        
        for row in cursor:
            songName = row[0]
            artistName = row[1]
            genre = row[2]
            album = row[3]
            length = row[4]
            

        playlistCursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES (?, ?, ?, ?, ?)', (songName, artistName, genre, album, length))

        newPlaylist.commit()
        
        addIndex = addIndex + 1

    
    playlistCursor.execute('SELECT songName, artistName, genre, album, length FROM songs')

    print("")

    for row in playlistCursor:
        print("| Song: ", row[0], end=" | ")
        print("Artist: ", row[1], end=" | ")
        print("Genre: ", row[2], end=" | ")
        print("Album: ", row[3], end=" | ")
        print("Length: ", row[4], " |")
    

    newPlaylist.close()

    playlist()


def playlistEdit():
    print("")
    print("Do you want to:")
    print("a) Add a song to a playlist")
    print("b) Remove a song from a playlist")
    print("c) Return to menu")
    answer = input("> ")

    if (answer == "a"):
        playlistAdd()
        
    elif (answer == "b"):
        playlistRemove()

    elif (answer == "c"):
        playlist()

    else:
        print("Invalid input.")
        playlistEdit()


def playlistAdd():
    print("")

    playlistName = input("Enter playlist name:")

    if os.path.isfile(playlistName + '.db'):
        pass

    else:
        print("That playlist does not exist.")
        playlistEdit()

    playlistDB = sqlite3.connect(playlistName + '.db')

    playlistCursor = playlistDB.cursor()

    print("While adding a song to a playlist")
    print("type \'exit\' at any time to return to the menu.")

    repeat = True
    
    while (repeat == True):
        print("")
        print("Enter song name (case sensitive):")
        song = input("> ")

        if (song == "exit"):
            playlistEdit()
            repeat = False

        elif (cursor.execute("SELECT songName FROM songs WHERE songName = ?",(song,)).fetchone()):
            repeat = False

        else:
            print("Invalid song name.")


    cursor.execute('SELECT songName, artistName, genre, album, length FROM songs WHERE songName = ?', (song,))
        
    for row in cursor:
        songName = row[0]
        artistName = row[1]
        genre = row[2]
        album = row[3]
        length = row[4]
            

    playlistCursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES (?, ?, ?, ?, ?)', (songName, artistName, genre, album, length))

    playlistDB.commit()

    playlistCursor.execute('SELECT songName, artistName, genre, album, length FROM songs')

    print("")

    for row in playlistCursor:
        print("| Song: ", row[0], end=" | ")
        print("Artist: ", row[1], end=" | ")
        print("Genre: ", row[2], end=" | ")
        print("Album: ", row[3], end=" | ")
        print("Length: ", row[4], " |")


    playlistDB.close()
    
    playlistEdit()


def playlistRemove():
    print("")

    playlistName = input("Enter playlist name:")

    if os.path.isfile(playlistName + '.db'):
        pass

    else:
        print("That playlist does not exist.")
        playlistEdit()


    playlistDB = sqlite3.connect(playlistName + '.db')

    playlistCursor = playlistDB.cursor()

    print("While adding a song to a playlist")
    print("type \'exit\' at any time to return to the menu.")

    repeat = True
    
    while (repeat == True):
        print("")
        print("Enter song name (case sensitive):")
        song = input("> ")

        if (song == "exit"):
            playlistEdit()
            repeat = False

        elif (playlistCursor.execute("SELECT songName FROM songs WHERE songName = ?",(song,)).fetchone()):
            repeat = False

        else:
            print("Invalid song name.")


    playlistCursor.execute('DELETE FROM songs WHERE songName = ?', (song,))

    playlistDB.commit()

    playlistCursor.execute('SELECT songName, artistName, genre, album, length FROM songs')

    print("")

    for row in playlistCursor:
        print("| Song: ", row[0], end=" | ")
        print("Artist: ", row[1], end=" | ")
        print("Genre: ", row[2], end=" | ")
        print("Album: ", row[3], end=" | ")
        print("Length: ", row[4], " |")


    playlistDB.close()
    
    playlistEdit()



def playlistView():
    print("")
    playlistName = input("Enter playlist name:")

    if os.path.isfile(playlistName + '.db'):
        pass

    else:
        print("That playlist does not exist.")
        playlist()


    playlistDB = sqlite3.connect(playlistName + '.db')

    playlistCursor = playlistDB.cursor()

    playlistCursor.execute('SELECT songName, artistName, genre, album, length FROM songs')

    print("")

    for row in playlistCursor:
        print("| Song: ", row[0], end=" | ")
        print("Artist: ", row[1], end=" | ")
        print("Genre: ", row[2], end=" | ")
        print("Album: ", row[3], end=" | ")
        print("Length: ", row[4], " |")


    playlistDB.close()

    playlist()


def searchSongs():
    print("")
    print("Do you want to:")
    print("a) Search all songs")
    print("b) Search by playlist")
    print("c) Return to menu")
    answer = input("> ")

    if (answer == 'a'):
        print("")
        print("Enter song name or type \'exit\' to return to menu.")
        repeat = True
    
        while (repeat == True):
            print("")
            print("Enter song name (case sensitive):")
            song = input("> ")

            if (song == "exit"):
                songMain()
                repeat = False

            elif (cursor.execute("SELECT songName FROM songs WHERE songName = ?",(song,)).fetchone()):
                repeat = False

            else:
                print("Invalid song name.")


        cursor.execute("SELECT songName, artistName, genre, album, length FROM songs WHERE songName = ?", (song,))

        print("")

        for row in cursor:
            print("| Song: ", row[0], end=" | ")
            print("Artist: ", row[1], end=" | ")
            print("Genre: ", row[2], end=" | ")
            print("Album: ", row[3], end=" | ")
            print("Length: ", row[4], " |")

        songMain()
        

    elif (answer == 'b'):
        print("")

        playlistName = input("Enter playlist name:")

        if os.path.isfile(playlistName + '.db'):
            pass

        else:
            print("That playlist does not exist.")
            searchSongs()

        playlistDB = sqlite3.connect(playlistName + '.db')

        playlistCursor = playlistDB.cursor()

        playlistCursor.execute('SELECT songName, artistName, genre, album, length FROM songs')
        
        print("")
        print("Enter song name or type \'exit\' to return to menu.")
        repeat = True
    
        while (repeat == True):
            print("")
            print("Enter song name (case sensitive):")
            song = input("> ")

            if (song == "exit"):
                songMain()
                repeat = False

            elif (playlistCursor.execute("SELECT songName FROM songs WHERE songName = ?",(song,)).fetchone()):
                repeat = False

            else:
                print("Invalid song name.")


        playlistCursor.execute("SELECT songName, artistName, genre, album, length FROM songs WHERE songName = ?", (song,))

        print("")

        for row in playlistCursor:
            print("| Song: ", row[0], end=" | ")
            print("Artist: ", row[1], end=" | ")
            print("Genre: ", row[2], end=" | ")
            print("Album: ", row[3], end=" | ")
            print("Length: ", row[4], " |")

        songMain()

    elif (answer == 'c'):
        songMain()

    else:
        print("Invalid input.")
        songMain()


def editAccount():
    print("")
    print("Do you want to:")
    print("a) Change your username")
    print("b) Change your password")
    print("c) Change your name")
    print("d) Change your email")
    print("e) Return to menu")
    answer = input("> ")

    if (answer == "a"):
        editUser()

    elif (answer == "b"):
        editPassword()

    elif (answer == "c"):
        editName()

    elif (answer == "d"):
        editEmail()

    elif (answer == "e"):
        songMain()

    else:
        print("Invalid input.")
        editAccount()
    
    songMain()


def editUser():
    userList = open("users.txt","r").read()
    userList = ast.literal_eval(userList)
    userIndex = userList[1].index(userLogin)
    
    print("")
    print("Type \'exit\' at any time to return to menu.")
    password = input("Enter password: ")

    if (password == 'exit'):
        editAccount()

    elif (password == userList[3][userIndex]):
        newUser = input("Enter new username: ")

        for character in newUser:
            if character not in verifyArray:
                print("Invalid input.")
                editUser()
                
        
        userList[1][userIndex] = newUser
        
        userAdd = open("users.txt","w")
        userAdd.write(str(userList))
        userAdd.close()

        editAccount()

    else:
        print("Incorrect password")
        editUser()


def editPassword():
    userList = open("users.txt","r").read()
    userList = ast.literal_eval(userList)
    userIndex = userList[1].index(userLogin)
    
    print("")
    print("Type \'exit\' at any time to return to menu.")
    password = input("Enter password: ")

    if (password == 'exit'):
        editAccount()

    elif (password == userList[3][userIndex]):
        def newPassword():
            newPassword = input("Enter new password: ")

            for character in newPassword:
                if character not in verifyArray:
                    print("Invalid input.")
                    editPassword()
            

            if (newPassword == 'exit'):
                editAccount()
            
            newPasswordConfirm = input("Please re-enter your new password: ")

            if (newPasswordConfirm == 'exit'):
                editAccount()

            elif (newPassword == newPasswordConfirm):
                userList[3][userIndex] = newPassword
                
                userAdd = open("users.txt","w")
                userAdd.write(str(userList))
                userAdd.close()

                editAccount()

            else:
                print("Passwords do not match.")
                newPassword()

    else:
        print("Incorrect password")
        editPassword()


def editName():
    userList = open("users.txt","r").read()
    userList = ast.literal_eval(userList)
    userIndex = userList[1].index(userLogin)
    
    print("")
    print("Type \'exit\' at any time to return to menu.")
    password = input("Enter password: ")

    if (password == 'exit'):
        editAccount()

    elif (password == userList[3][userIndex]):
        newName = input("Enter new name: ")

        for character in newName:
            if character not in verifyArray:
                print("Invalid input.")
                editName()
        
        
        userList[0][userIndex] = newName
        
        userAdd = open("users.txt","w")
        userAdd.write(str(userList))
        userAdd.close()

        editAccount()

    else:
        print("Incorrect password")
        editName()


def editEmail():
    userList = open("users.txt","r").read()
    userList = ast.literal_eval(userList)
    userIndex = userList[1].index(userLogin)
    
    print("")
    print("Type \'exit\' at any time to return to menu.")
    password = input("Enter password: ")

    if (password == 'exit'):
        editAccount()

    elif (password == userList[3][userIndex]):
        newEamil = input("Enter new E-mail: ")

        for character in newEmail:
            if character not in verifyArray:
                print("Invalid input.")
                editEmail()

        if ("@" in newEmail and "." in newEmail and " " not in newEmail and newEmail.count("@") == 1):
            userList[2][userIndex] = newEmail
        
            userAdd = open("users.txt","w")
            userAdd.write(str(userList))
            userAdd.close()

            editAccount()

        else:
            print("Invalid input.")
            editEmail()
        

    else:
        print("Incorrect password")
        editEmail()


print("")
print("Welcome to The Music Program.")

verifyArray = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",".","_","-","@"," "]

db = sqlite3.connect('spotify.db')

cursor = db.cursor()

main()

db.close()
