import pandas as pd
import matplotlib.pyplot as plt
import os


plt.style.use('fivethirtyeight')


# list the files
PATH = '/Users/genius/PycharmProjects/CHOAS/Data/'

filelist = os.listdir(PATH)

filelist1 = [file for file in filelist if file not in ['.DS_Store', 'matrix_dc.txt', 'matrix_emu.txt']]
filelist1.sort()

filelist2 = [file for file in filelist if file in ['matrix_dc.txt', 'matrix_emu.txt']]
filelist2.sort()

# read them into pandas
df_list1 = [pd.read_csv(PATH + file, names=['a', 'b']) for file in filelist1]
df_list2 = [pd.read_csv(PATH + file, names=['a', 'b']) for file in filelist2]

df_list1A = df_list1[:3]
df_list1B = df_list1[3:]
for df in df_list1B:
    df.sort_values(by='a', inplace=True)

fig1, ax1 = plt.subplots(nrows=2, ncols=3, figsize=(21, 16))
fig2, ax2 = plt.subplots(nrows=2, ncols=1, figsize=(21, 8))
title = ['Random', 'Predator-Prey', 'Mixture', 'Competition', 'Mutualism']


j = 0
for col in ax1[0]:
    col.scatter(df_list1A[j].a, df_list1A[j].b, s=2)
    col.set_xlim(-20, 20)
    col.set_ylim(-20, 20)
    col.set_xlabel('Re')
    col.set_ylabel('Im')
    plt.setp(col.get_yticklabels()[0], visible=False)
    plt.setp(col.get_yticklabels()[-1], visible=False)
    plt.setp(col.get_xticklabels()[0], visible=False)
    plt.setp(col.get_xticklabels()[-1], visible=False)
    col.set_title(title[j])
    j += 1

j = 0
for col in ax1[1]:
    if j == 1:
        print(len(df_list1B[0]))
        col.set_xlim(-1, 7)
        col.set_ylim(-0.1, 1.1)

    else:
        col.set_xlim(-1, 3)
        col.set_ylim(-0.1, 1.1)

    col.scatter(df_list1B[j].a, df_list1B[j].b)
    col.set_xlabel('K')
    col.set_ylabel('P(stability)')
    plt.setp(col.get_yticklabels()[0], visible=False)
    plt.setp(col.get_yticklabels()[-1], visible=False)
    plt.setp(col.get_xticklabels()[0], visible=False)
    plt.setp(col.get_xticklabels()[-1], visible=False)
    col.set_title(title[j])
    j += 1


i = 0
for row in ax2:
    if i == 0:
        row.set_xlim(-60, 20)
        row.set_ylim(-10, 10)
    else:
        row.set_xlim(-20, 60)
        row.set_ylim(-10, 10)

    row.scatter(df_list2[i].a, df_list2[i].b, s=2)
    row.set_xlabel('Re')
    row.set_ylabel('Im')
    plt.setp(row.get_yticklabels()[0], visible=False)
    plt.setp(row.get_yticklabels()[-1], visible=False)
    plt.setp(row.get_xticklabels()[0], visible=False)
    plt.setp(row.get_xticklabels()[-1], visible=False)
    row.set_title(title[3:][i])
    i += 1


plt.show()
fig1.savefig('fig2.pdf', dpi=1200, format='pdf')
fig1.savefig('fig2.png', dpi=1200, format='png')
fig2.savefig('fig3.pdf', dpi=1200, format='pdf')
fig2.savefig('fig3.png', dpi=1200, format='png')
