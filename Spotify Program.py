
import ast


# Example of a function
def main():
    print("")
    print("Would you like to:")
    print("a) Sign in")
    print("b) Sign up")
    print("c) End program")
    answer = input("> ") # Example of a variable

    # Example of an if else statement
    if (answer == "a"):
        login()
        
    elif (answer == "b"):
        register()

    elif (answer == "c"):
        pass

    elif (answer == "x"):
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

                    if (newPassword == "exit"):
                        main()

                    else:
                        print("")
                        newPasswordVerify = input("Please re-enter your password here:")

                        if (newPasswordVerify == "exit"):
                            main()

                        else:
                            registerAdd()

                        

                    #registerPassword end



                print("")
                newEmail = input("Please enter your e-mail here:")

                
                if (newEmail == "exit"):
                    main()

                else:
                    registerPassword()
                
                #registerEmail end

                

            print("")
            newUser = input("Please enter your username here:")


            if (newUser == "exit"):
                main()
        
            elif (newUser in userList[1]
                  ):
                print("Unfortunately, that username already exists.")
                print("Please try another username.")
                registerUser()

            else:
                registerEmail()

            #registerUser end



        print("")
        newName = input("Please enter your name here:")
        
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
    print("d) Edit account details")
    print("e) Sign out")
    answer = input("> ")


    
    if (answer == "a"):
        listSongs()

    elif (answer == "b"):
        sortSongs()

    elif (answer == "c"):
        playlist()

    elif (answer == "d"):
        editAccount()

    elif (answer == "e"):
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
    print("")

    songList = open("songs.txt","r").read()
    songList = ast.literal_eval(songList)
    
    songListLength = len(songList)
    songListIndex = 0
    
    
    while (songListIndex < songListLength):
        songIndex = 0
        print("| Song: " + str(songList[songListIndex][songIndex]),end=" | ")
        songIndex = songIndex + 1

        print("Artist: " + str(songList[songListIndex][songIndex]),end=" | ")
        songIndex = songIndex + 1

        print("Genre: " + str(songList[songListIndex][songIndex]),end=" | ")
        songIndex = songIndex + 1

        print("Album: " + str(songList[songListIndex][songIndex]),end=" | ")
        songIndex = songIndex + 1

        print("Length: " + str(songList[songListIndex][songIndex]),end=" | ")

        songListIndex = songListIndex + 1

        print("")
        

    
    songMain()



def sortSongs():
    songList = open("songs.txt","r").read()
    songList = ast.literal_eval(songList)
    
    songListLength = len(songList)
    songListIndex = 0
    
    print("")
    print("Do you want to list songs by:")
    print("a) Name")
    print("b) Artist")
    print("c) Genre")
    print("d) Album")
    print("e) Length")
    answer = input("> ")

    if (answer == "a"):
        print("")

        # Name sort end

    elif (answer == "b"):
        sortList = []

        while (songListIndex < songListLength):
            addList = []
            addList.append(songList[songListIndex][1])
            addList.append(songList[songListIndex][0])
            sortList.append(addList)

            songListIndex = songListIndex + 1

        print("Do you want to:")
        print("a) Sort from A - Z")
        print("b) Sort from Z - A")
        answer = input("> ")
        if (answer == "a"):
            sortList = sorted(sortList)
            

        elif (answer == "b"):
            sortList = sorted(sortList, reverse = True)

        

        # Artist sort end

    elif (answer == "c"):
        print("")

        # Genre sort end

    elif (answer == "d"):
        print("")

        # Album sort end

    elif (answer == "e"):
        print("")

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
            print("Returning to main menu.")
            songMain()

    
    songMain()


def playlist():
    print("")


    """

    songList = open("songs.txt","r").read()
    songList = ast.literal_eval(songList)
    
    songListLength = len(songList)

    
    if ("The Black Hit Of Space" in songList[0]):
        print(songList[0].index("The Black Hit Of Space"))
    
    """
    songMain()


def editAccount():
    print("")
    songMain()


print("")
print("Welcome to The Music Program.")



main()


