# -*- coding: utf-8 -*-
import numpy as np

def encontra_elemento(elemento):
    tabela = np.array([['H','','','','','','','','','','','','B','C','N','O','F','NE'],['LI','BE','','','','','','','','','','','B','C','N','O','F','NE'],['NA','MG','','','','','','','','','','','AL','SI','P','S','CL','AR'],['K','CA','SC','TI','V','CE','MN','FE','CO','NI','CU','ZN','GA','GE','AS','SE','BR','KR'],['RB','SR','Y','ZR','NB','MO','TC','RU','RH','PD','AG','CD','LN','SN','SB','TE','L','XE'],['CS','BA','MUITO1','HF','TA','W','RE','OS','LR','PT','AU','HG','TI','PB','BI','PO','AT','RN'],['FR','RA','MUITO2','RF','DB','SG','BH','HS','MT','DS','RG','CN','NH','FL','MC','LV','TS','OG']])

    MUITO1 = ['LA','CE','PR','ND','PM','SM','EU','GD','TB','DY','HO','ER','TM','YB','LU']
    MUITO2 = ['AC','TH','PA','U','NP','PU','AM','CM','BK','CF','ES','FM','MD','NO','LR']

    familiaB = [2,3,4,5,6,7,8,9,10,11] #so precisa familia B





    familia = ''
    familia_periodo = ''
    Localizando_o_elemento = np.where(tabela == elemento)     

    (linha,coluna) = Localizando_o_elemento 
        
      #  "classificando as familias"
    print(type(coluna))
    if coluna not in familiaB:
        familia = 'A'
        
    else:
        familia = "B"
        if coluna == 7 or coluna == 8 or coluna == 9:
            coluna = 7
        elif coluna == 10:
            coluna = 0
        elif coluna == 11:
            coluna = 1
        else:
            pass
     #  '________________________'
        
    familia_periodo = ("Elemento pertence a familia {}{} de periodo {}".format(int(coluna+1),familia,int(linha+1)))

    print(familia_periodo)
        
    return familia_periodo


    


print("<<<<<<<<<<<<<<<<<<<<<<Periodic table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("H\nLi","Be                              B  C  N  O  F  Ne\nNa","Mg                              Al Si P  S  Cl Ar\nK"," Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr\nRb","Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe\nCs","Ba   Hf Ta W  Re Os Ir Pt Au Hg Ti Pb Bi Po At Rn\nFr","Ra   Rf Db Sg Bh Hs Mt Ds Rg Cn Nh FI Mc Lv Ts Og")
print("_____________________________________________________\n")



elemento = input("qual elemento? ") 

#encontra_elemento(elemento)

"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!-----proximo passo deletar linha de cod , e substituir metodo de achar eletrons etc os valores----- !!!!!!!!!!!!!"








elementos_eletro = {'F':3.98,"O":3.44,"Cl":3.16,'N':3.04,'Br':2.96,'I':2.66,'S':2.58,
                    'Ac':0.7,"La":0.79,'Sr':0.82,'Ce':0.89,'Th':0.89,'Na':0.93,'Y':0.95,
                    'Li':0.98,'K':0.82,'Pr':1.1,'Pa':1.1,'Nd':1.12,'Pm':1.13,'Sm':1.14,
                    'Gd':1.17,"Dy":1.2,'Zr':1.22,'Er':1.22,'Tm':1.23,'Yb':1.24,'Lu':1.25,
                    'Ta':1.27,'Cm':1.28,'W':1.3,'U':1.3,'Bk':1.3,'Cf':1.3,'Es':1.3,
                    'Fm':1.3,'Md':1.3,'No':1.3,'Lr':1.3,'Rf':1.3,'Db':1.3,'Mg':1.31,
                    'Nb':1.31,'Ca':1.36,'Am':1.36,'Pu':1.38,'Re':1.5,'Np':1.5,'Sc':1.54,
                    'Cr':1.55,'Be':1.57,'Mo':1.6,'Al':1.61,'Bi':1.62,'Ti':1.63,'Cu':1.65,
                    'V':1.66,'ln':1.69,'Sn':1.78,'Zn':1.81,'Mn':1.83,'Fe':1.88 ,'Si':1.9,
                    'Ni':1.9,'Ru':1.9,'Ir':1.9,'Co':1.91,'Cd':1.93,'Sb':1.96 ,'Pb':2,
                    'Rn':2,'Ga':2.01,'At':2.02,'B':2.04,'I':2.05,'Xe':2.1,'Tc':2.16,
                    'As':2.18,'P':2.19,'H':2.2,'Rh':2.26,'Ag':2.2,'Pt':2.2,'Au':2.2,
                    'Fr':2.24,'Pd':2.28,'Hg':2.28,'Po':2.33,'Os':2.36,'TI':2.54,'C':2.55,
                    'Se':2.55,'S':2.58,'Ba':2.6,'Cs':2.66,'Kr':2.96,'Rb':0.8}

while True:
    elemento = input("Escolha o elemento \ncaso queira parar digite PARE\n")
    if elemento == "PARE":
        break
    else:
        for i in elementos_eletro:
            if i.lower() == elemento.lower():
                print(elementos_eletro[i])
                print("found")


print('!source : https://www.lenntech.com/periodic/elements/rb.htm' )

