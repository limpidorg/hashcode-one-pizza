import repackage

repackage.up()

from utils import getClients

clients = getClients("A.txt")
print(clients)
