from random import randint #This imports the randint function so I can randomize which phrase will be chosen

def live(lives,difference): #This method checks the # of the user's lives. The difference variable is explained in the lettercheck method
           lives = lives - difference
           return lives

def letterCheck(guess, phrase, blankphrase,lives): #This method checks if the guessed letter exists within the word. If it does it replacesthe blank phrase with the letters in the same place that they exist in the phrase. This makes it seem like the blank phrase is being slowly replaced with the right letters. 
           difference = 1 #This difference variable is to seet the lives. If the guess is not in the word, the difference is set to 1. If it is, the difference is set to 0. This difference is then sent to the live method above which will either result in the live variable decreasing (if difference is 1) or staying the same (if difference is 0)
           if guess in phrase:
                      for i in range(0, len(phrase)):
                                 if (phrase[i] == guess):
                                            blankphrase[i] = guess
                                            difference = 0
           print(blankphrase)
           return difference

def answer(): #This method turns the list into a string.
           newphrase = ""
           for i in phrase:
                      newphrase = newphrase + i  
           return newphrase

def fail(failed): #This keeps track of which letters have been guessed which are incorrect. This is so that it can be displayed to the user so that the user doesn't make the same mistake again.
           if guess not in phrase:
                      failed = failed + guess
           return failed
           
failed = "" #This sets the failed variable to blank, which will later be filled.
lives = 6 #This sets the number of lives the user has before they lose 
phraselist = [ ["b","a","n","a","n","a"] , ["s","t","r","a","w","b","e","r","r","y"], ["d","o","l","p","h","i","n"], ["c","o","m","p","u","t","e","r"] , ["g","r","a","v","i","t","y"] ]
num = randint(0,5) #This generates a random num, which will then choose which word the user has to guess.
phrase = (phraselist[num]) 
newphrase = answer()
blankphrase = ["_"]*len(phrase) #This sets the blank phrase which the user needs to fill in
print(blankphrase) 

while lives > 0: #This allows the user to guess as long as they still have lives left         
           print("\nYou have", lives, "lives left") # This broadcasts how many lives the user has left
           print("Wrong letters: ",failed) #This shows which wrong letters they have already guessed
           guess = input("Guess a letter: ") #Asks for a number, but stores it as a string so that it can be manipulated like a string (word finding)            
           guess = guess.lower()
           failed = fail(failed)
           if guess == newphrase: #If the user puts in the answer, this will make it so that they instantly win.
                      print("\nCongratulations! You won!")
                      print("Word:",newphrase)
                      break            
           difference = letterCheck(guess, phrase, blankphrase,lives) #This sends the guess to the above method so that it can be related to the phrase, and replace the corerect letters, if the guess is correct
           lives = live(lives,difference) #This updates the lives variable if the guess is incorrect
           if blankphrase == phrase: #If the user completely fills the blank phrase with the correct letters, they get the win message, and the code ends
                      print("\nCongratulations! You won!")
                      print("Word:",newphrase)
           if lives == 6:
                print ("+---+")
                print ("    |   ")
                print ("    |   ")  
                print ("    |   ")
                print ("    === ")
           if lives == 5:
                print ("+---+")
                print (" O  |   ")
                print ("    |   ")  
                print ("    |   ")
                print ("    === ") 
           if lives == 4:
                print ("+---+")
                print (" O  |   ")
                print (" |  |   ")  
                print ("    |   ")
                print ("    === ")
           if lives == 3:
                print ("+---+")
                print (" O  |   ")
                print ("/|  |   ")  
                print ("    |   ")
                print ("    === ")  
           if lives == 2:
                print ("+---+")
                print (" O  |   ")
                print ("/|\ |   ")  
                print ("    |   ")
                print ("    === ") 
           if lives == 1:
                print ("+---+")
                print (" O  |   ")
                print ("/|\ |   ")  
                print ("/   |   ")
                print ("    === ") 
           if lives == 0: #If the user ruuns out of lives, they recieve the game over message
                print ("+---+")
                print (" O  |   ")
                print ("/|\ |   ")  
                print ("/ \ |   ")
                print ("    === ") 
                print("\nSorry! You lost!")
                print("The word was:",)
                print(newphrase)
                break

