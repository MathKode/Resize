import os
from PIL import Image
from numpy import asarray
import numpy as np
def reduc(nb1,nb2) : #Retourne la fraction irréductible 
    Ls_nb1 = []
    Ls_nb2 = []
    nb = 1
    while True :
        if int(nb1) % nb == 0 :
            Ls_nb1.append(nb)
        if int(nb2) % nb == 0 :
            Ls_nb2.append(nb)
        if nb > int(nb1) and nb > int(nb2) :
            break
        nb+=1
    Ls_nb1 = Ls_nb1[::-1]
    Ls_nb2 = Ls_nb2[::-1]
    com_div = 0
    for div_nb1 in Ls_nb1 :
        if div_nb1 in Ls_nb2 :
            com_div = div_nb1
            break
    nb1 = int(int(nb1) / com_div)
    nb2 = int(int(nb2) / com_div)
    print(nb1,nb2)
    return nb1, nb2

def resize(x,y,way) :
    x = int(x)
    y = int(y)
    # Ce code va à chaque tour diviser par 2 Mais, quand il atteindra un nombre inférieur à final x ou y, il calculera le rapoprt
    data = asarray(Image.open(str(way))).copy()
    data_ls = []
    #Transforme le tableau numpy en ls
    data_ls = []
    for line in data :
        l = []
        for i in line :
            l.append(list(i))
        data_ls.append(l)
    #print(data_ls)
    img_y = data.shape[0] #shape 0 = y
    img_x = data.shape[1]

    # Y resize (/2) :

    while int(img_y / 2) > y :
        if img_y % 2 != 0 :
            img_y -= 1
        ls = []
        d = 0 #Variable disant si on garde ou non la ligne
        tour = 0 #Vr servant a ne prendre que img_y ligne 
        for i in data_ls :
            if d == 0 and tour < img_y :
                ls.append(i)
                d = 1
            else :
                d = 0
            tour += 1
        print(len(ls),img_y,data.shape[0])
        data_ls = ls
        img_y = img_y / 2
    print(len(ls),img_y,data.shape[0])
    #Trouve la fraction irréductible :
    num_y, den_y = reduc(y,img_y)
    ls = []
    d = 0
    for i in data_ls :
        if d > den_y - 1 :
            d = 0
        if d < num_y :
            ls.append(i)
        d += 1
    data_ls = ls
    print(len(data_ls))

    # X resize (/2) :

    while int(img_x / 2) > x :
        if img_x % 2 != 0 :
            img_x -= 1
        ls = []
        for line in data_ls :
            line_ls = []
            d = 0
            tour = 0
            for colonne in line :
                if d == 0 and tour < img_x :
                    line_ls.append(colonne)
                    d = 1
                else :
                    d = 0
                tour += 1
            ls.append(line_ls)
        data_ls = ls
        print(len(data_ls[0]),img_x,data.shape[1])
        img_x = img_x / 2
    #Trouve la fr irréductible :
    num_x, den_x = reduc(x,img_x)
    ls = []
    for line in data_ls :
        line_ls = []
        d = 0
        for i in line :
            if d > den_x - 1 :
                d = 0
            if d < num_x :
                line_ls.append(i)
            d += 1
        ls.append(line_ls)
    data_ls = ls
    print(len(data_ls[0]),img_x,data.shape[1])

    #Egalise les pixels (pour qu'il y est que du RGB et pas du RGBv ou RGBa)
    print(data_ls[0][0])
    while len(data_ls[0][0]) > 3 :
        for line in data_ls :
            for i in line :
                del i[-1]
    print(data_ls[0][0])
    data_final = np.array(data_ls)
    imagefinal = Image.fromarray(data_final)
    imagefinal.save("lol.png") 
    
if __name__ == "__main__":
    x, y = input("Chose the final X Y : ").split()
    print('')
    lsf = os.listdir();n=1
    for i in lsf : print("  ",n,i);n+=1
    print("")
    choix = int(input('Number of the file : '))
    filename = lsf[choix-1]
    print(filename)
    resize(x,y,filename)
    