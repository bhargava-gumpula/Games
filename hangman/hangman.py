# coding: utf-8
import random as r
name_list = ["Fortnite", "Minecraft", "Roblox", "Game of thrones", "Gears of War", "Pokemon", "Motoracer 4"]
name = r.choice(name_list)
lives = 0

# Get the difficulty level from user
# this will decide nameber of life lines
while True:
  level = input('''  EASY 1
  MEDIUM = 2
  HARD = 3
  :''')
  if level == 1:
     lives = 12
  elif level == 2:
     lives = 8
  elif level == 3:
     lives = 4
  else:
     print "Wrong level selected"
     continue

  break

# Make and print the right amount of hearts
# Actual guessing and matching part
while True:
   heart_symbol = "❤️ "
   total_lives = heart_symbol * lives
   print ("You have %s lives") % (total_lives)
   guess = raw_input("Guess a type of video game:")

   if guess.upper() == name.upper():
      print ("Wow you guessed right. you win YAY!")
      break

   lives = lives - 1
   if lives < 1:
      print("You lost the game. The correct word is %s. Better luck next time bye!") % (name)
      break

   print("That's an incorect guess, try again")
