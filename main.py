import time, os
a=input("Welcome to the Star Wars Quiz. \nOnly a few people get over 80%. Would you like to play \n(WARNING: THIS QUIZ MAY CONTAIN SPOILERS FOR MANY STAR WARS\nMOVIES,TV SHOWS, ETC.)\n--> ").lower()
def clear():
  os.system("clear")
clear()
if a in ["yes", "yep", "y", "yeet"]:
  print("Great, let's start")
  time.sleep(2)
  clear()
  os.system("python3 ....py")
  c=0
  i=0
#______________
  q1=input("The TIE Fighter flown by Moff Gideon is called... \nA-TIE X32 or B-Outland TIE- ").lower()
  if q1=="b":
    print("Correct")
    c+=1
  else:
    print("Incorrect")
    i+=1
  print("\n")
#______________
  q2=input("How many passengers could the HAVw A6 Juggernaut hold.\nA-300 or B-200- ").lower()
  if q2=="a":
    print("Correct")
    c+=1
  else:
    print("Incorrect")
    i+=1
  print("\n")
#______________
  q3=input("When he died, Kylo Ren (Ben Solo) was\nA-35 or B-30 years old- ").lower()
  if q3=="b":
    print("Correct")
    c+=1
  else:
    print("Incorrect")
    i+=1
  print("\n")
#______________
  q4=input("The BLT-B Y-wing was produced during this war...\nA-Galactic Civil or B-Clone Wars- ").lower()
  if q4=="b":
    print("Correct")
    c+=1
  else:
    print("Incorrect")
    i+=1
  print("\n")
#______________
  q5=input("The Arquitens-class light cruiser had (A-3 or B-5) months\nof consumables- ").lower()
  if q5=="a":
    print("Correct")
    c+=1
  else:
    print("Incorrect")
    i+=1
  print("\n")
#______________
  q6=input("What sniper rifle does/did Din Djarin carry...\nA-Modified DLT-19X B-Amban Sniper Rifle- ").lower()
  if q6=="b":
    print("Correct")
    c+=1
  else:
    print("Incorrect")
    i+=1
  print("\n")
#______________
  q7=input("The RK-3 blaster pistol was made by...\nA-SonnBlas B-MerrSon- " ).lower()
  if q7=="b":
    print("Correct")
    c+=1
  else:
    print("Incorrect")
    i+=1
  print("\n")
#______________
  q8=input("The official name for the Death Star (1) plans was called Project...\nA-Star Dust B-Omega One- ").lower()
  if q8=="a":
    print("Correct")
    c+=1
  else:
    print("Incorrect")
    i+=1
  print("\n")
#______________
  q9=input("Sabine Wren weilded this ancient mandalorian weapon...\nA-The Darksaber B-Dual WESTAR-35 pistols- ").lower()
  if q9=="a":
    print("Correct\n")
    c+=1
  else:
    print("Incorrect\n")
    i+=1
#______________
  q10=input("Qui Gon Jin was an apprentice to this jedi master...\nA-Mace Windu B-Count Dooku- ").lower()
  if q10=="b":
    print("Correct\n")
    c+=1
  else:
    print("Incorrect\n")
    i+=1
#______________
  q11=input("Captain Phasma's awesome armor was made from this material... \nA-Titanium B-Chromium- ").lower()
  if q11=="b":
    print("Correct\n")
    c+=1
  else:
    print("Incorrect\n")
    i+=1
#______________
  q12=input("The E-11D was designed for...\nA-Close combat B-Long range combat- ").lower()
  if q12=="a":
    print("Correct\n")
    c+=1
  else:
    print("Incorrect\n")
    i+=1
#______________
  q13=input("The ELG-3A was used by this person...\nA-Padme Amidala B-Rey Palpatine- ")
  if q13=="a":
    print("Correct")
    c+=1
  else:
    print("Incorrect")
    i+=1
#______________
  t=13
#______________
  score1=c/t
  score=round(score1*100)
  clear()
  os.system("python3 ....py")
  print("For your final score, you got...")
  time.sleep(3)
  print("You got",c,"correct and",i,"incorrect. Or a",score)
else:
  print("Hmm, you must not be a TRUE Star Wars Nerd")