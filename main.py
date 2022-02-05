import repackage

repackage.up()

from utils import getClients

clients, ingredients = getClients("A.txt")
print(clients)
print("=================")
print(ingredients)
