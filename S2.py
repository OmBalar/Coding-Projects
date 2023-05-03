n = int(input())

names = input()
partners = input()

nameList = names.split(" ")
partnerList = partners.split(" ")

counter = 0
for name in nameList:

    partner = partnerList[counter]

    index = nameList.index(partner)
    nameHere = partnerList[index]

    if name != nameHere or partner != nameList[index] or name == partner:
        print("bad")
        break
    
    if counter == len(nameList) - 1:
        print("good")

    counter += 1

