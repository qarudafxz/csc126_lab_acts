import random
import os

class RockPaperScissors(object):
    ai = ""
    ai_score = 0

    def __init__(self, player, score, city, school, birth_month, option):
     self.player = player
     self.score = score
     self.city = city
     self.school = school
     self.birth_month = birth_month
     self.option = option
     self.score1 = 0
     self.ai_score = 0

    def define_score(self):
     self.score1 = 0
     self.ai_score = 0

    def compare(self, choice):
     file = open("game.txt", "a+")
     self.ai = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])

     file.write(f"You choose: {choice}\n")
     print("You choose:", choice)
     file.write(f"Computer choose: {self.ai}\n")
     print("Computer choose:", self.ai)

     choices = {
         "Rock": ["Scissors", "Lizard"],
         "Paper": ["Rock", "Spock"],
         "Scissors": ["Paper", "Lizard"],
         "Lizard": ["Spock", "Paper"],
         "Spock": ["Rock", "Scissors"]
     }

     if choice not in choices:
         file.write("Invalid choice, please try again!\n")
         print("Invalid choice, please try again!")
         return

     if choice == self.ai:
         file.write("It's a tie!\n")
         print("It's a tie!")
     elif self.ai in choices[choice]:
         self.score1 += 1
         file.write(f"{self.player} wins!\n")
         print(self.player, "wins!")
     else:
         self.ai_score += 1
         file.write("Computer wins!\n")
         print("Computer wins!")

    def main(self):
     file = open("game.txt", "a+")
     self.define_score()
     print("===== Welcome to the Rock-Paper-Scissors-Lizard-Spock Game! =====")
     file.write("\n\n\n===== Welcome to the Rock-Paper-Scissors-Lizard-Spock Game! =====\n")

     while self.score1 < 3 and self.ai_score < 3:
       user_choice = input("Choose between: Rock, Paper, Scissors, Lizard, and Spock and type it here: ")
       file.write(f"Choose between: Rock, Paper, Scissors, Lizard, and Spock and type it here: {user_choice}\n")

       self.compare(user_choice)
       file.write(f"{self.player}  scored {self.score1} and the computer scored {self.ai_score}\n")
       print(f"{self.player}  scored {self.score1} and the computer scored {self.ai_score}")

     if self.score1 > self.ai_score:
       file.write("Congratulations! You win!")
       print("Congratulations! You win!")
     else:
       file.write("You lose, AI wins!")
       print("You lose, AI wins!")

     print("Do you want to play again?")
     self.option = input("Type 'yes' to play again or 'no' to exit: ")
     if self.option == "yes":
         self.main()
     else:
         print("Thank you for playing!")
         file.close()
         os._exit(0)

first_name = input("Please enter player's first name: ")
last_name = input("Please enter player's last name: ")
city = input("Please enter player's city: ")
school = input("Please enter player's school: ")
birth_month = input("Please enter player's birth month: ")

game = RockPaperScissors(player=first_name + " " +last_name, score=0, city=city, school=school, birth_month=birth_month, option="")
game.main()