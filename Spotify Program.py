
import ast



def main():
    print("")
    print("Would you like to:")
    print("a) Sign in")
    print("b) Sign up")
    print("c) End program")
    answer = input("> ")


    if (answer == "a"):
        login()
        
    elif (answer == "b"):
        register()

    elif (answer == "c"):
        pass
        
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
        
            elif (newUser in userList):
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
    userList = open("users.txt","r").read()
    userList = ast.literal_eval(userList)

    print("")
    print("Please enter your sign in information.")
    global userLogin
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



def listSongs():
    print("")



def sortSongs():
    print("")



def playlist():
    print("")



def editAccount():
    print("")



print("")
print("Welcome to The Music Program.")



main()


