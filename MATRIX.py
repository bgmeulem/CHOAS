import numpy as np

numSpecies = 2
Sigma = 1
Chance = 0.8

CommunityMatrix = np.zeros((numSpecies, numSpecies))
for i in range(0, numSpecies):
    for j in range(0, numSpecies):
        randomvar1 = np.random.random()
        if randomvar1 <= Chance:
            randomvar2 = np.random.random()
            if randomvar2 <= 0.5:
                Mij = abs(np.random.normal(0, Sigma))
                CommunityMatrix[i][j], CommunityMatrix[j][i] = Mij, -Mij
        else:
            CommunityMatrix[i][j], CommunityMatrix[j][i] = 0, 0


print(CommunityMatrix)