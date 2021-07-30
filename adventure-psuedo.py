#Tharma Philogene, Emmanuel

# Diamond_room
def Diamond_room():
  "Now you entered the room of a monster!"
  "The monster is sleeping. Behind the monster, there is another door. What would you do? (1 or 2) "
  "Go through the door silently"
  "Kill the monster and show your courage"
  # '\n' is to print the line in a new line
  print("Now you entered the room of a monster!")
  print("The monster is sleeping. Behind the monster, there is another door. What would you do? (1 or 2)")
  print("1). Go through the door silently.")
  print("2). Kill the monster and show your courage!")

  # get user input take input()
answer = input (">")
if answer == "1" : 
    print("The player lost the diamond.")
elif answer == "2" : 
    print("the player is dead.")
else: 
  print("game_over, and start again.")

def Gold_room():
  "Now you entered the Gold_room!"
  # '\n' is to print the line in a new line
  print("Now you entered the Gold_room!")

  # get user input take input()

  if answer == "1" :
    print("lead the player to the Silver_room")
  elif answer == "2" :
    print("The player will gain 2 gold and a diamond.")
  else:
    print("The player goes back to Diamond_room")

def Silver_room():
  "Now you entered the room of Cooper!"
  # '\n' is to print the line in a new line
  print("Now you entered the room of Cooper!")

  # get user input take input()

  if answer == "2" :
    print("The player win, and gain 5 gold, 5 diamond.")
  elif answer == "1" :
    print("The player goes back to diamond_room")
  else:
     print("game_over you lost your live")

# function to ask play again or not
def play_again():
  print(" do you want to play again? y/n")
  # get input
  answer = input(">").lower
  # evaluate input using conditional 
  if answer == "y": 
    print ("start()")
  else:
     #if player types anything besides "yes" or "y", exit() the program 
     print("exit()")

# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  "You lost your life. Go to Diamond_room or watch a video"
  print( "You lost your life. Go to Diamond_room or watch a video")
  print("Game Over!")
  # STRETCH: maybe ask player to play again or not. 
  play_again()


def start():
  # have some introductory text printed like: ("\nYou are standing in a dark room.")
  print("You are in the Forest. It is dark, and you need to go home.")
  # get user input using input() and save 
  answer = input(">")

  #use a loop to manage game -- 
if "x" in answer:
  Diamond_room()
    #go to a function()
elif "y" in answer :
  Gold_room()
    #go to another function()
    # go somewhere else
elif "h" in answer :
  Silver_room()
    # go somewhere else
else:
  #game_over()
    # else go to game over function because wrong input - game over 
  print(game_over("Don't you know how to type something properly?"))


# calling start function. 
start()
