from mod_char import * 
from mod_party import *
import random

    
def game_logger(message):  
  game_log = open("game_log.txt", "a+")
  game_log.write(message + "\n")
  
def cast_skill(member, boss, choice):
    choice = random.randint(0, 1)
    if isinstance(member, Swordsman):
        skill = member.attack if choice == 0 else member.thrust
    elif isinstance(member, Wizard):
        skill = member.attack if choice == 0 else member.cast_spell
    elif isinstance(member, Archer):
        skill = member.attack if choice == 0 else member.precision_shot
    else:
        skill = None
    
    if skill:
        print(skill(boss))
        game_logger(skill(boss))


def boss_fight(party, boss):
 choice = 0
 while boss.is_alive():
  for member in party.members:
   cast_skill(member, boss, choice)
   
  target_player = random.choice(party.members)
  boss_choice = random.randint(0, 1)
  
  if(boss_choice == 0):
   print(boss.attack(target_player))
   game_logger(boss.attack(target_player))
  else:
   print(boss.special_attack(target_player))
   game_logger(boss.special_attack(target_player))
  
  if not target_player.is_alive():
   party.members.remove(target_player)
   print(f"{target_player.name} has been killed!")
   game_logger(f"{target_player.name} has been killed!")
  
  for member in party.members:
   if isinstance(member, Healer):
    print(member.heal(target_player))
    game_logger(member.heal(target_player))
    break
   
  print(f"Boss Health: {boss.health}")
  
 print("Boss is defeated!")
    

def main(): 
 player1 = Swordsman("Francis Dualweilder")
 player2 = Wizard("Gandalf Spell")
 player3 = Healer("Miss Jasmin The Healer")
 player4 = Archer("Robin Hood")
 party = Party()
 
 boss = BossMonster()
 
 print(party.add_member(player1))
 print(party.add_member(player2))
 print(party.add_member(player3))
 print(party.add_member(player4))
 
 print("Party members: ", party.party_info())
 
 print("\n\n\n\n\n ===========WELCOME TO SWORD ART ONLINE============ \n\n\n\n\n")
 
 if(party.members):
  boss_fight(party, boss)
 
if(__name__ == "__main__"):
 main()