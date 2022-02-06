import repackage

repackage.up()

from operator import itemgetter
import time

from utils import getClients, getAllIngredientImpacts

FILENAME = "C"
FILE_PATH = f"./testFiles/{FILENAME}.txt"

startTime = time.time()

clients, ingredients, pClients = getClients(FILE_PATH)
userscores = [0] * pClients
ingredientsImpact = getAllIngredientImpacts(ingredients, clients, userscores)

clientSorted = []
for client in clients:
    meanImpact = 0
    dislikeCount = 0
    if client[1]:
        for dislike in client[1]:
            meanImpact += ingredientsImpact[dislike]
            dislikeCount += 1
    else:
        meanImpact += ingredientsImpact[""]
        dislikeCount += 1

    clientSorted.append([meanImpact / dislikeCount, client])

clientSorted = sorted(clientSorted, key=itemgetter(0))
clientSorted = list(reversed(clientSorted))

approvedClients = []
approvedLikes = []
approvedDislikes = []
for i in range(len(clientSorted)):
    client = clientSorted[i][1]
    clientDislikes = client[1]
    clientLikes = client[0]

    if (
        not any(x in approvedLikes for x in clientDislikes)
        and not any(x in approvedDislikes for x in clientLikes)
        or clientDislikes == []
    ):
        approvedClients.append(clientSorted[i])

        for ingredient in client[0]:
            approvedLikes.append(ingredient)
        for ingredient in client[1]:
            approvedDislikes.append(ingredient)

res = []
for i in approvedLikes:
    if i not in res:
        res.append(i)

print("\n")
print(f"Ingredients count : {len(res)}")
print(f"Ingredients list : {res}")
print(f"Number of clients : {len(approvedClients)} / {len(clients)}")

with open(f"./answers/{FILENAME}.txt", "w") as f:
    f.write(f"Ingredients count : {len(res)}\n")
    f.write(f"Ingredients list : {res}\n")
    f.write(f"Number of clients : {len(approvedClients)} / {len(clients)}")


print(f"\n Successfully written to ./answers/{FILENAME}.txt")

print("\n--- Executed in %s seconds ---" % (time.time() - startTime))
