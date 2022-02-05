def getClients(filename):
    with open(filename) as f:
        lines = f.readlines()

    linesChanged = []
    for line in lines:
        lineToChange = line.replace("\n", "")
        linesChanged.append(lineToChange)

    pClients = int(linesChanged[0])

    clients = []
    linesChanged.pop(0)

    for i in range(0, pClients * 2, 2):
        print(linesChanged[i])
        likes = []
        dislikes = []

        for j in range(2):
            lineElements = linesChanged[i + j].split(" ")

            if j == 0:
                for x in range(len(lineElements)):
                    if x != 0:
                        likes.append(lineElements[x])
            elif j == 1:
                for x in range(len(lineElements)):
                    if x != 0:
                        dislikes.append(lineElements[x])

        clients.append([likes, dislikes])

    return clients
