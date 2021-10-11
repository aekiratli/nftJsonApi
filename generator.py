import random
import json

MAX_SUPPLY = 36
TOKEN_URI = "https://example.com/images/"

stopCounter = 0
attr0 = [0,1,2,3,4,5]
attr1 = [0,1,2]
attr2 = [0,1]
attr0value = ["orc","wood elf","dark elf","night elf","dwarf","human"]
attr1value = ["muscular","skinny","fat"]
attr2value = ["sword","bow"]
attr0len = len(attr0)
attr1len = len(attr1)
attr2len = len(attr2)
genAttr0 = []
genAttr1 = []
genAttr2 = []

unqId = []
unqAttr = []
generate = True

while(generate):

    tokenId = random.randint(0,MAX_SUPPLY)

    if (not tokenId in unqId):

        attr0Id = random.randint(0,attr0len-1)
        attr1Id = random.randint(0,attr1len-1)
        attr2Id = random.randint(0,attr2len-1)
        unqChecker = str(attr1Id) + str(attr0Id) + str(attr2Id)

        if (unqChecker in unqAttr):

            pass

        else:
            stopCounter = stopCounter + 1
            unqAttr.append(unqChecker)
            unqId.append(tokenId)
            genAttr0.append(attr0Id)
            genAttr1.append(attr1Id)
            genAttr2.append(attr2Id)

    if (stopCounter == MAX_SUPPLY):

        generate = False

jsonList = []



for i in range(0,MAX_SUPPLY):
    jsonList.append({"tokenId" : i,
                    "race" : attr0value[genAttr0[i]],
                     "body build" : attr1value[genAttr1[i]],
                     "weapon": attr2value[genAttr2[i]],
                     "tokenUri": TOKEN_URI+unqAttr[i]+".png"})

jsonList = json.dumps(jsonList, indent = 1)

file = open('nfts.json', 'w')
file.truncate()
file.write(jsonList)
file.close()