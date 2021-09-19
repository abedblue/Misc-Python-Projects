import xlwt
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

wb = xlwt.Workbook()
style1 = xlwt.easyxf(num_format_str='0.00')
ws = wb.add_sheet('SmiteAPI Data')

file = open("C:\Users\Abe\Documents\jsTextFile2.txt", "r")

fileString = file.read()

myStringList = fileString.split("{")

iterator = 1

myStringList.remove("")

for subString in myStringList:
    #print(subString[subString.index('Account_Level') + 15: subString.index(',"ActiveId1"')])
    if iterator > 65535:
        ws = wb.add_sheet('SmiteAPI Data-ext')
        iterator = 0
    ws.write(iterator, 0, subString[subString.index('Account_Level') + 15: subString.index(',"ActiveId1"')])
    
    #rather than printing, output it to the excel sheet in the format of smiteapidatainitial in python nonsense.

    ws.write(iterator, 1, subString[subString.index('"Assists":') + 10: subString.index(',"Ban1":')])
    ws.write(iterator, 2, subString[subString.index('"Ban1":') + 7: subString.index(',"Ban10":')])
    ws.write(iterator, 3, subString[subString.index('"Ban2":') + 7: subString.index(',"Ban2Id":')])
    ws.write(iterator, 4, subString[subString.index('"Ban3":') + 7: subString.index(',"Ban3Id":')])
    ws.write(iterator, 5, subString[subString.index('"Ban4":') + 7: subString.index(',"Ban4Id":')])
    ws.write(iterator, 6, subString[subString.index('"Ban5":') + 7: subString.index(',"Ban5Id":')])
    ws.write(iterator, 7, subString[subString.index('"Ban6":') + 7: subString.index(',"Ban6Id":')])
    ws.write(iterator, 8, subString[subString.index('"Ban7":') + 7: subString.index(',"Ban7Id":')])
    ws.write(iterator, 9, subString[subString.index('"Ban8":') + 7: subString.index(',"Ban8Id":')])
    ws.write(iterator, 10, subString[subString.index('"Conquest_Tier":') + 16: subString.index(',"Conquest_Wins":')])
    ws.write(iterator, 11, subString[subString.index('"Damage_Bot":') + 13: subString.index(',"Damage_Done_In_Hand":')])
    ws.write(iterator, 12, subString[subString.index('"Damage_Done_In_Hand":') + 22: subString.index(',"Damage_Done_Magical":')])
    ws.write(iterator, 13, subString[subString.index('"Damage_Done_Magical":') + 22: subString.index(',"Damage_Done_Physical":')])
    ws.write(iterator, 14, subString[subString.index('"Damage_Done_Physical":') + 23: subString.index(',"Damage_Mitigated":')])
    ws.write(iterator, 15, subString[subString.index('"Damage_Mitigated":') + 19: subString.index(',"Damage_Player":')])
    ws.write(iterator, 16, subString[subString.index('"Damage_Player":') + 16: subString.index(',"Damage_Taken":')])
    ws.write(iterator, 17, subString[subString.index('"Damage_Taken":') + 15: subString.index(',"Damage_Taken_Magical":')])
    ws.write(iterator, 18, subString[subString.index('"Damage_Taken_Magical":') + 24: subString.index(',"Damage_Taken_Physical":')])
    ws.write(iterator, 19, subString[subString.index('"Damage_Taken_Physical":') + 25: subString.index(',"Deaths":')])
    ws.write(iterator, 20, subString[subString.index('"Deaths":') + 9: subString.index(',"Distance_Traveled":')])
    ws.write(iterator, 21, subString[subString.index('"Distance_Traveled":') + 20: subString.index(',"Duel_Losses":')])
    ws.write(iterator, 22, subString[subString.index('"Duel_Tier":') + 12: subString.index(',"Duel_Wins":')])
    ws.write(iterator, 23, subString[subString.index('"Final_Match_Level":') + 20: subString.index(',"First_Ban_Side":')])
    ws.write(iterator, 24, subString[subString.index('"First_Ban_Side":') + 17: subString.index(',"GodId":')])
    ws.write(iterator, 25, subString[subString.index('"Gold_Earned":') + 14: subString.index(',"Gold_Per_Minute":')])
    ws.write(iterator, 26, subString[subString.index('"Gold_Per_Minute":') + 18: subString.index(',"Healing":')])
    ws.write(iterator, 27, subString[subString.index('"Healing":') + 10: subString.index(',"Healing_Bot":')])
    ws.write(iterator, 28, subString[subString.index('"Healing_Bot":') + 14: subString.index(',"Healing_Player_Self":')])
    ws.write(iterator, 29, subString[subString.index('"Healing_Player_Self":') + 23: subString.index(',"ItemId1":')])
    ws.write(iterator, 30, subString[subString.index('"Item_Active_1":') + 16: subString.index(',"Item_Active_2":')])
    ws.write(iterator, 31, subString[subString.index('"Item_Active_2":') + 16: subString.index(',"Item_Active_3":')])
    ws.write(iterator, 32, subString[subString.index('"Item_Purch_1":') + 15: subString.index(',"Item_Purch_2":')])
    ws.write(iterator, 33, subString[subString.index('"Item_Purch_2":') + 15: subString.index(',"Item_Purch_3":')])
    ws.write(iterator, 34, subString[subString.index('"Item_Purch_3":') + 15: subString.index(',"Item_Purch_4":')])
    ws.write(iterator, 35, subString[subString.index('"Item_Purch_4":') + 15: subString.index(',"Item_Purch_5":')])
    ws.write(iterator, 36, subString[subString.index('"Item_Purch_5":') + 15: subString.index(',"Item_Purch_6":')])
    ws.write(iterator, 37, subString[subString.index('"Item_Purch_6":') + 15: subString.index(',"Joust_Losses":')])
    ws.write(iterator, 38, subString[subString.index('"Joust_Tier":') + 13: subString.index(',"Joust_Wins":')])
    ws.write(iterator, 39, subString[subString.index('"Kills_Bot":') + 12: subString.index(',"Kills_Double":')])
    ws.write(iterator, 40, subString[subString.index('"Kills_Fire_Giant":') + 19: subString.index(',"Kills_First_Blood":')])
    ws.write(iterator, 41, subString[subString.index('"Kills_First_Blood":') + 20: subString.index(',"Kills_Gold_Fury":')])
    #ws.write(iterator, 41, subString[subString.index('"Joust_Tier":') + 13: subString.index(',"Joust_Wins":')])
    ws.write(iterator, 42, subString[subString.index('"Kills_Gold_Fury":') + 18: subString.index(',"Kills_Penta":')])
    ws.write(iterator, 43, subString[subString.index('"Kills_Phoenix":') + 16: subString.index(',"Kills_Player":')])
    ws.write(iterator, 44, subString[subString.index('"Kills_Player":') + 15: subString.index(',"Kills_Quadra":')])
    ws.write(iterator, 45, subString[subString.index('"Mastery_Level":') + 16: subString.index(',"Match":')])
    ws.write(iterator, 46, subString[subString.index('"Minutes":') + 10: subString.index(',"Multi_kill_Max":')])
    ws.write(iterator, 47, subString[subString.index('"Objective_Assists":') + 20: subString.index(',"PartyId":')])
    ws.write(iterator, 48, subString[subString.index('"Reference_Name":') + 17: subString.index(',"Region":')])
    ws.write(iterator, 49, subString[subString.index('"Region":') + 9: subString.index(',"Skin":')])
    ws.write(iterator, 50, subString[subString.index('"Structure_Damage":') + 19: subString.index(',"Surrendered":')])
    ws.write(iterator, 51, subString[subString.index('"Surrendered":') + 14: subString.index(',"TaskForce":')])
    ws.write(iterator, 52, subString[subString.index('"Time_In_Match_Seconds":') + 25: subString.index(',"Towers_Destroyed":')])
    ws.write(iterator, 53, subString[subString.index('"Towers_Destroyed":') + 19: subString.index(',"Wards_Placed":')])
    ws.write(iterator, 54, subString[subString.index('"Wards_Placed":') + 15: subString.index(',"Win_Status":')])
    ws.write(iterator, 55, subString[subString.index('"Win_Status":') + 13: subString.index(',"Winning_TaskForce":')])
    ws.write(iterator, 56, subString[subString.index('"playerId":') + 12: subString.index(',"playerName":') -1 ])

    #s = iterator, 56, subString[subString.index('"playerName":') + 13: subString.index(',"ret_msg":')]
    iterator += 1

wb.save("C:\Users\Abe\Documents\Python Nonsense\SmiteAPIDataOutput4.xls")
