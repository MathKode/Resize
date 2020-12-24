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
    #Trouve la fraction irréductible :
    num_y, den_y = reduc(y,img_y)
    num_y_new = int(den_y/(int(den_y/num_y) + 1))
    print('new_y',num_y_new)
    reste = num_y - num_y_new
    print(reste)
    diviseur = int(img_y/den_y) #donne le nombre de pour den_x * ? = img_x
    print('div =',diviseur)
    ls = []
    d = 0
    tour = 0
    px_add = 0
    for line in data_ls :
        if d == 0 :
            #print('ok',tour,px_add)
            ls.append(line)
            px_add += 1
            d = 1
        elif tour < int(reste * diviseur*2) :
            #print('ok2',tour,px_add)
            px_add += 1
            ls.append(line)
            d = 0
        else :
            d = 0
        tour += 1
    erreur = len(ls)-y #Calcul les lignes en trop
    print('er',erreur)
    #Supp ligne en trop
    d = 0
    for i in range(erreur) :
        if d == 0 :
            del ls[-1]
            d = 1
        else :
            del ls[0]
            d = 0
    
    print(int(reste * diviseur*2))
    data_ls = ls
    print(len(data_ls),img_y,data.shape[0])

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
    #Calcul : Ex : num = 75, den = 128 : 128/75 = 1,5 = 2 128/2 = 64  75-64 = 11 
    num_x_new = int(den_x/(int(den_x/num_x) + 1))
    print('new_x',num_x_new)
    reste = num_x - num_x_new
    print(reste)
    diviseur = int(img_x/den_x) #donne le nombre de pour den_x * ? = img_x
    ls = []
    for line in data_ls :
        line_ls = []
        d = 0
        tour = 0
        px_add = 0
        for i in line :
            if d == 0 :
                #print('ok',tour,px_add)
                line_ls.append(i)
                px_add += 1
                d = 1
            elif tour < int(reste * diviseur*2) :
                #print('ok2',tour,px_add)
                px_add += 1
                line_ls.append(i)
                d = 0
            else :
                d = 0
            tour += 1
        ls.append(line_ls)
    print(int(reste * diviseur*2))
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
    