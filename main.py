from ast import operator
import repackage

repackage.up()

from operator import itemgetter

from utils import getClients, getAllIngredientImpacts

clients, ingredients = getClients("A.txt")
userscores = [0, 0, 0]
ingredientsImpact = getAllIngredientImpacts(ingredients, clients, userscores)

clientSorted = []
for client in clients:
    clientSorted.append([ingredientsImpact["".join(client[1])], client])

clientSorted = sorted(clientSorted, key=itemgetter(0))

approvedClients = []
approvedLikes = []
for i in range(len(clientSorted)):
    client = clientSorted[i][1]
    clientDislikes = client[1]

    if not all(x in approvedLikes for x in clientDislikes) or clientDislikes == []:
        approvedClients.append(clientSorted[i])

        for ingredient in client[0]:
            approvedLikes.append(ingredient)


res = []
for i in approvedLikes:
    if i not in res:
        res.append(i)

print(f"Ingredients count : {len(res)}")
print(f"Ingredients list : {res}")
print(f"Number of clients : {len(approvedClients)} / {len(clients)}")
