from hashlib import new
import numpy as np 
import random
from random import randint

import matplotlib.pyplot as plt
import pandas as pd



def generate_PNJ(difficulty_lvl, job_role=None):
    """
    Génère un PNJ avec un niveau de difficulté donnée

    Cela génère une liste de 6 integer, représentant les stats du PNJ.
    Chaque integer ce situe entre entre un minimum et un maximum selon la difficulté donnée.
    
    La liste est générée en fonction des poids "p"

    :param difficulty_lvl: Le niveau de difficulté du PNJ
    :return: Une liste de 6 int
    """
    points = 56+difficulty_lvl

    stats = ["arm", "dext", "intel", "mana", "pv", "str"]
    poids = [1/6*0.8, 1/6*0.9, 1/6, 1/6, 1/6*1.4, 1/6*0.9]
    if job_role == "Heal":
        poids = [1/6*0.7, 1/6, 1/6*1.3, 1/6, 1/6, 1/6]
    # if job_role == "Tank":
    #     pass

    nr = np.random.choice(stats,
            size=points, 
            replace=True,
            p=poids)

    unique, counts = np.unique(nr, return_counts=True) # 
    a = dict(zip(unique, counts))
    return a


def generate_PNJ2(difficulty_lvl):
    """
    Generate a PNJ with a given difficulty level

    It generates a list of 6 numbers, each number being between the minimum and maximum possible values
    for a given difficulty level
    
    :param difficulty_lvl: The difficulty level of the PNJ
    :return: A list of 6 integers.
    """
    points = 56 + difficulty_lvl
    max_points = int(points/4)
    min_points = int(points/11.4)

    r = [0 for i in range(0,6)]
    total_points = 0

    while total_points < points:
        for i in range(0,6):
            dice = randint(min_points, max_points)

            futur_attribute = r[i] + dice

            futur_total_points = total_points + futur_attribute
            if futur_total_points > points:
                r[i] += points - total_points
                total_points += points - total_points
            else:
                r[i] = futur_attribute
                total_points += futur_attribute
    
    #  format json {'arm': 12, 'dext': 3, 'intel': 13, 'mana': 9, 'pv': 7, 'str': 12}
    a = {'arm': str(r[5]), 'dext': str(r[3]), 'intel': str(r[4]), 'mana': str(r[1]), 'pv': str(r[0]), 'str': str(r[2])}
    
    return a


old = []
new = []
for i in range(0,2000):
    old.append(generate_PNJ2(10))
    new.append(generate_PNJ(10))


# plot a repartition of arm, dex, intel, mana, pv, str for old array
arm = []
dext = []
intel = []
mana = []
pv = []
str = []
for i in old:
    arm.append(int(i['arm']))
    dext.append(int(i['dext']))
    intel.append(int(i['intel']))
    mana.append(int(i['mana']))
    pv.append(int(i['pv']))
    str.append(int(i['str']))



# plot a repartition of arm, dex, intel, mana, pv, str for new array
armNew = []
dextNew = []
intelNew = []
manaNew = []
pvNew = []
strNew = []
for i in new:
    armNew.append(int(i['arm']))
    dextNew.append(int(i['dext']))
    intelNew.append(int(i['intel']))
    manaNew.append(int(i['mana']))
    pvNew.append(int(i['pv']))
    strNew.append(int(i['str']))

# plot 6 figures for arm, dex, intel, mana, pv, str
plt.figure(1)
plt.subplot(221)
plt.title('arm')
plt.hist(arm, bins=10, alpha=0.5, label='arm')
plt.hist(armNew, bins=10,color='red', alpha=0.5, label='arm new')
# show labels

plt.subplot(223)
plt.title('dext')
plt.hist(dext, bins=10, alpha=0.5, label='dext')
plt.hist(dextNew, bins=10,color='red', alpha=0.5, label='dext new')

plt.subplot(222)
plt.title('intel')
plt.hist(intel, bins=10, alpha=0.5, label='intel')
plt.hist(intelNew, bins=10,color='red', alpha=0.5, label='intel new')

plt.subplot(224)
plt.title('mana')
plt.hist(mana, bins=10, alpha=0.5, label='mana')
plt.hist(manaNew, bins=10,color='red', alpha=0.5, label='mana new')

plt.figure(2)
plt.subplot(221)
plt.title('pv')
plt.hist(pv, bins=10, alpha=0.5, label='pv')
plt.hist(pvNew, bins=10,color='red', alpha=0.5, label='pv new')


plt.subplot(223)
plt.title('str')
plt.hist(str, bins=10, alpha=0.5, label='str')
plt.hist(strNew, bins=10,color='red', alpha=0.5, label='str new')



# resizing the figures
fig1 = plt.figure(1)
fig1.set_size_inches(5, 5)
fig2 = plt.figure(2)
fig2.set_size_inches(5, 5)

# show the figures
plt.show()

