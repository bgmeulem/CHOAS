import numpy as np
from Matrix import WillekeurigeMatrix, PredatorPreyMatrix, MixtureMatrix, eig_values
from tqdm import tqdm
import time

# 0.1, 0.1 for Random
# 0.4 , 0.1 for PP
sig = np.random.normal(0.1, 0.1, 200)
sig_pp = np.random.normal(0.4, 0.1, 200)
C = 0.25
species = 250
repeats = 750

boek_w = {}
boek_p = {}
boek_mi = {}

file_w = open('stability_aw.txt', 'w')
file_p = open('stability_bp.txt', 'w')
file_mi = open('stability_cmi', 'w')

for sigm, sigm_pp in tqdm(zip(sig, sig_pp)):
    sigm, sigm_pp = abs(sigm), abs(sigm_pp)

    K = sigm * np.sqrt(C * species)
    K_pp = sigm_pp * np.sqrt(C * species)
    boek_mi[K] = 0
    boek_p[K_pp] = 0
    boek_w[K] = 0

    for iterator in tqdm(range(0, repeats)):

        time.sleep(0.1)

        Matrixw = WillekeurigeMatrix(species=species, sigma=sigm, C=C, d=1)
        Matrixp = PredatorPreyMatrix(species=species, sigma=sigm_pp, C=C, d=1)
        Matrixmi = MixtureMatrix(species=species, sigma=sigm, C=C, d=1)

        eigval_re_w, eigval_im_w = eig_values(Matrixw)
        eigval_re_p, eigval_im_p = eig_values(Matrixp)
        eigval_re_mi, eigval_im_mi = eig_values(Matrixmi)

        if (eigval_re_w <= 0).all():
            boek_w[K] += 1/repeats

        if (eigval_re_p <= 0).all():
            boek_p[K_pp] += 1/repeats

        if (eigval_re_mi <= 0).all():
            boek_mi[K] += 1/repeats

for sleutel, sleutel_pp in zip(boek_w, boek_p):

    file_w.write('{},{}\n'.format(sleutel, boek_w[sleutel]))
    file_p.write('{},{}\n'.format(sleutel_pp, boek_p[sleutel_pp]))
    file_mi.write('{},{}\n'.format(sleutel, boek_mi[sleutel]))

file_w.close()
file_p.close()
file_mi.close()
