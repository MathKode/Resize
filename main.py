import os
from PIL import Image
from numpy import asarray
import numpy as np

def reduc(nb1,nb2) :
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
    #Ouvrir l'img concerné :
    data = asarray(Image.open(str(way))).copy()
    """ INUTILE POUR CE CODE mais on sait jamais ^^
    #Creation de l'image final
    shape_final = []
    for i in range(int(y)) :
        l = []
        for j in range(int(x)) :
            l.append([0,0,0])
        shape_final.append(l)
    data_final = np.array(shape_final,dtype=np.uint8)
    print(data_final)
    """
    #resize largeur :
    nb2 = data.shape[1] #shape 1 = x
    print('x',nb2,x)
    numerateur_x, denominateur_x = reduc(x,nb2)
    numerateur_x = int(numerateur_x);denominateur_x = int(denominateur_x)
    nb1 = data.shape[0] #shape 0 = y
    print("y",nb1,y)
    numerateur_y, denominateur_y = reduc(y,nb1)
    numerateur_y = int(numerateur_y);denominateur_y = int(denominateur_y)
    nb_line = 0
    line_final = 0
    """
    for i in data :
        for j in i :
            print(j,end=' / ')
        print('')
    """

    data_ls = []
    for line in data :
        l = []
        for i in line :
            l.append(list(i))
        data_ls.append(l)
    #print(data_ls)
    print("numerateur y :",numerateur_y)
    print("denominateur y :",denominateur_y)
    print("numerateur x :",numerateur_x)
    print("denominateur_x :",denominateur_x)
    ls_ligne = [] #toutes les lignes selectionnées
    tour = 0
    nombre_ligne = 0
    for i in data_ls :
        if nombre_ligne > denominateur_y -1 :
            nombre_ligne = 0
        if nombre_ligne < numerateur_y :
            #print('ok',nombre_ligne,tour)
            ls_ligne.append(data_ls[tour])
        tour += 1
        nombre_ligne += 1
    #for i in ls_ligne :
        #print(i)
    
    ls_final = []
    tour = 0
    nombre_ligne : 0
    for line in ls_ligne :
        ls_co = []
        nombre_colonne = 0
        for i in line :
            if nombre_colonne > denominateur_x - 1 :
                nombre_colonne = 0
            if nombre_colonne < numerateur_x :
                ls_co.append(i)
            nombre_colonne += 1
        #print(ls_co)
        ls_final.append(ls_co)

    for line in ls_final :
        for i in line :
            del i[-1]
    #print(ls_final)
    print(len(ls_final))
    data_final = np.array(ls_final)
    imagefinal = Image.fromarray(data_final)
    imagefinal.save("lol.png") 
    


if __name__ == "__main__":
    x_final, y_final = input("Chose the final X Y : ").split()
    print(x_final,y_final);print("")
    lsf = os.listdir();n=1
    for i in lsf : print("  ",n,i);n+=1
    print("")
    choix = int(input('Number of the file : '))
    filename = lsf[choix-1]
    print(filename)
    resize(x_final,y_final,filename)
