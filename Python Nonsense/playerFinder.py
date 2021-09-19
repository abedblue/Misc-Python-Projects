file = open("C:\Users\Abe\Documents\jsTextFile2.txt", "r")

fileString = file.read()

myStringList = fileString.split("{")

iterator = 1

myStringList.remove("")

for subString in myStringList:
    #print(subString[subString.index('Account_Level') + 15: subString.index(',"ActiveId1"')])
    if subString[subString.index('"playerId":') + 12: subString.index(',"playerName":') -1 ] == '873290':
        print(subString[subString.index('"playerName":') + 13: subString.index(',"ret_msg":')])
