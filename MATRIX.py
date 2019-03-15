import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time


plt.style.use('fivethirtyeight')


def WillekeurigeMatrix(species=250, sigma=1, C=0.25, d=1):
    Matrix = np.zeros((species, species))
    for i in range(0, species):
        for j in range(0, i+1):
            if i == j:
                Matrix[i][j] = -d
            else:
                randomvar1 = np.random.random()
                if randomvar1 <= C:
                    Mij, Mji = np.random.normal(0, sigma, 2)
                    Matrix[i][j], Matrix[j][i] = Mij, Mji

                else:
                    Matrix[i][j], Matrix[j][i] = 0, 0

    return Matrix


def PredatorPreyMatrix(species=250, sigma=1, C=0.25, d=1):

    Matrix = np.zeros((species, species))
    for i in range(0, species):
        for j in range(0, i+1):
            if i == j:
                Matrix[i][j] = -d
            else:
                randomvar1 = np.random.random()
                if randomvar1 <= C:
                    randomvar2 = np.random.random()
                    if randomvar2 <= 0.5:
                        Mij = abs(np.random.normal(0, sigma))
                        Mji = - abs(np.random.normal(0, sigma))
                        Matrix[i][j], Matrix[j][i] = Mij, Mji
                    else:
                        Mij = - abs(np.random.normal(0, sigma))
                        Mji = abs(np.random.normal(0, sigma))
                        Matrix[i][j], Matrix[j][i] = Mij, Mji

                else:
                    Matrix[i][j], Matrix[j][i] = 0, 0

    return Matrix


def CompetitionMatrix(species=250, sigma=1, C=0.25, d=1):

    Matrix = np.zeros((species, species))
    for i in range(0, species):
        for j in range(0, i+1):
            if i == j:
                Matrix[i][j] = -d
            else:
                randomvar1 = np.random.random()
                if randomvar1 <= C:
                    Mij = - abs(np.random.normal(0, sigma))
                    Mji = - abs(np.random.normal(0, sigma))
                    Matrix[i][j], Matrix[j][i] = Mij, Mji

                else:
                    Matrix[i][j], Matrix[j][i] = 0, 0

    return Matrix


def MutualismMatrix(species=250, sigma=1, C=0.25, d=1):
    Matrix = np.zeros((species, species))
    for i in range(0, species):
        for j in range(0, i+1):
            if i == j:
                Matrix[i][j] = -d

            else:
                randomvar1 = np.random.random()
                if randomvar1 <= C:
                    Mij = abs(np.random.normal(0, sigma))
                    Mji = abs(np.random.normal(0, sigma))
                    Matrix[i][j], Matrix[j][i] = Mij, Mji

                else:
                    Matrix[i][j], Matrix[j][i] = 0, 0

    return Matrix


def MixtureMatrix(species=250, sigma=1, C=0.25, d=1):

    Matrix = np.zeros((species, species))
    for i in range(0, species):
        for j in range(0, i+1):
            if i == j:
                Matrix[i][j] = -d

            else:
                randomvar1 = np.random.random()
                if randomvar1 <= C:
                    randomvar2 = np.random.random()
                    if randomvar2 <= 0.5:
                        Mij, Mji = abs(np.random.normal(0, sigma, 2))
                        Matrix[i][j], Matrix[j][i] = Mij, Mji
                    else:
                        Mij, Mji = - abs(np.random.normal(0, sigma, 2))
                        Matrix[i][j], Matrix[j][i] = Mij, Mji

                else:
                    Matrix[i][j], Matrix[j][i] = 0, 0

    return Matrix


def calculate_eig_values(matrix):
    eigval, eigvec = np.linalg.eig(matrix)
    eigval_re = eigval.real
    eigval_im = eigval.imag

    return eigval_re, eigval_im


fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(21, 7))
fig1, ax1 = plt.subplots(nrows=2, ncols=1, figsize=(7, 7))


for test in tqdm(range(0, 10)):

    time.sleep(0.1)

    Matrixw = WillekeurigeMatrix()
    Matrixp = PredatorPreyMatrix()
    Matrixc = CompetitionMatrix()
    Matrixmu = MutualismMatrix()
    Matrixmi = MixtureMatrix()

    eigval_re_w, eigval_im_w = calculate_eig_values(Matrixw)
    eigval_re_p, eigval_im_p = calculate_eig_values(Matrixp)
    eigval_re_c, eigval_im_c = calculate_eig_values(Matrixc)
    eigval_re_mu, eigval_im_mu = calculate_eig_values(Matrixmu)
    eigval_re_mi, eigval_im_mi = calculate_eig_values(Matrixmi)

    teplotten1 = [(eigval_re_w, eigval_im_w), (eigval_re_p, eigval_im_p), (eigval_re_mi, eigval_im_mi)]
    titel1 = ['Willekeurig', 'Predator-Prey', 'Mixture']

    teplotten2 = [(eigval_re_mu, eigval_im_mu), (eigval_re_c, eigval_im_c)]
    titel2 = ['Mutualism', 'Competition']

    i = 0
    for col in ax:
        col.scatter(teplotten1[i][0], teplotten1[i][1], s=2)
        col.set_xlim(-20, 20)
        col.set_ylim(-20, 20)
        col.set_xlabel('Re')
        col.set_ylabel('Im')
        col.set_title(titel1[i])
        i += 1

    j = 0
    for col in ax1:
        col.scatter(teplotten2[j][0], teplotten2[j][1], s=2)
        col.set_xlim(-60, 60)
        col.set_ylim(-5, 5)
        col.set_xlabel('Re')
        col.set_ylabel('Im')
        col.set_title(titel2[j])
        j += 1


plt.show()

