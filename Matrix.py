import numpy as np
from tqdm import tqdm
import time


def WillekeurigeMatrix(species=250, sigma=1., C=0.25, d=1):
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


def PredatorPreyMatrix(species=250, sigma=1., C=0.25, d=1):

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


def CompetitionMatrix(species=250, sigma=1., C=0.25, d=1):

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


def MutualismMatrix(species=250, sigma=1., C=0.25, d=1):
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


def MixtureMatrix(species=250, sigma=1., C=0.25, d=1):

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


def eig_values(matrix):
    eigval, eigvec = np.linalg.eig(matrix)
    eigval_re = eigval.real
    eigval_im = eigval.imag

    return eigval_re, eigval_im


def Plot():

    file_w = open('matrix_aw.txt', 'w')
    file_p = open('matrix_bp.txt', 'w')
    file_mi = open('matrix_cmi.txt', 'w')
    file_c = open('matrix_dc.txt', 'w')
    file_mu = open('matrix_emu.txt', 'w')

    for blank in tqdm(range(0, 10)):

        time.sleep(0.1)

        Matrixw = WillekeurigeMatrix(species=250, sigma=1, C=0.25, d=1)
        Matrixp = PredatorPreyMatrix(species=250, sigma=1, C=0.25, d=1)
        Matrixc = CompetitionMatrix(species=250, sigma=1, C=0.25, d=1)
        Matrixmu = MutualismMatrix(species=250, sigma=1, C=0.25, d=1)
        Matrixmi = MixtureMatrix(species=250, sigma=1, C=0.25, d=1)

        re_w, im_w = eig_values(Matrixw)
        re_p, im_p = eig_values(Matrixp)
        re_c, im_c = eig_values(Matrixc)
        re_mu, im_mu = eig_values(Matrixmu)
        re_mi, im_mi = eig_values(Matrixmi)

        for a, b, c, d, e, f, g, h, i, j in zip(re_w, im_w, re_p, im_p, re_mi, im_mi, re_c, im_c, re_mu, im_mu):
            file_w.write('{},{}\n'.format(a, b))

            file_p.write('{},{}\n'.format(c, d))

            file_mi.write('{},{}\n'.format(e, f))

            file_c.write('{},{}\n'.format(g, h))

            file_mu.write('{},{}\n'.format(i, j))


    file_w.close()
    file_p.close()
    file_mi.close()
    file_c.close()
    file_mu.close()
