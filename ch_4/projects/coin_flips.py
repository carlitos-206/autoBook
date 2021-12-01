#crete coin flip and pass result in list
#loop 10k
#check for a 6 in a row 

import random
list=[]
streaks= 0
counter=0
for i in range(10000):
    result = random.randint(0,1)
    if result == 0:
        list.append("H")
    else:
        list.append("T")
H=list.count("H")
# print(list)
print(f"H appears: {H}")
for i in range(len(list)):
    if list[i]=="T":
        counter=0
        # print("reset", counter)
    if list[i]=="H":
        counter+=1
        # print("counted", counter)
    if counter==6:
        streaks+=1
        counter=0
        # print("Streak", streaks)
print(f"Streaks of 6: {streaks}")
base = 10000
h_streak = base/6
chance = round(((streaks/h_streak)*100), 2)
print(f"Chance of a streak of 6: ~{chance}%")
h_chance = round(((H/base)*100), 2) 
print(f"Chance of H: ~{h_chance}%")
