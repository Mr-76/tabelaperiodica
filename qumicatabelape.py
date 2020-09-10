print("<<<<<<<<<<<<<<<<<<<<<<Tabela Periodica>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("H\nLi","Be                              B  C  N  O  F  Ne\nNa","Mg                              Al Si P  S  Cl Ar\nK"," Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr\nRb","Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe\nCs","Ba   Hf Ta W  Re Os Ir Pt Au Hg Ti Pb Bi Po At Rn\nFr","Ra   Rf Db Sg Bh Hs Mt Ds Rg Cn Nh FI Mc Lv Ts Og")
print("_____________________________________________________")












f1a=("H",'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr')
f2a=('Be', 'Ca', 'Mg', 'Sr', 'Ba','Ra')
f3a=('B', 'Al', 'Ga', 'In', 'Tl')
f4a=('C', 'Si', 'Ge', 'Sn', 'Pb')
f5a=['N', 'P', 'As', 'Sb', 'Bi']
f6a=('O', 'S', 'Se', 'Te', 'Po')
f7a=('F', 'Cl', 'Br', 'I', 'At')
f8a=('He', 'Ne', 'Ar', 'Kr' , 'Xe', 'Rn')
f1b =("Cu","Ag","Au","Rg")
f2b =("Zn","Cd","Hg","Uub") 
f3b =("Sc","Y","Lu","Lr")
f4b =("Ti","Zr","Hf","Rf") 
f5b =("V","Nb","Ta","Db") 
f6b =("Cr","Mo","W","Sg") 
f7b =("Mn","Tc","Re","Bh")
f8b =("Fe","Ru","Rh","Os","Hs","Mt","Ir","Rh","Co","Ni","Pd","Pt","Ds") 





a=input('\nGet the family of the element \n enter the name of the element in the same way is int the table:  ')




if a in f1a:
    print ('FAMILY 1A')
if a in f2a:
    print ('FAMILY 2A')    
if a in f3a:
    print ('FAMILY 3A') 
if a in f4a:
    print ('FAMILY 4A')
if a in f5a:
    print ('FAMILY 5A')    
if a in f6a:
    print ('FAMILY 6A') 
if a in f7a:
    print ('FAMILY 7A')
if a in f8a:
    print ('FAMILY 8A')    
if a in f1b:
    print ('FAMILY 1B')
if a in f2b:
    print ('FAMILY 2B')    
if a in f3b:
    print ('FAMILY 3B') 
if a in f4b:
    print ('FAMILY 4B')
if a in f5b:
    print ('FAMILY 5B')    
if a in f6b:
    print ('FAMILY 6B') 
if a in f7b:
    print ('FAMILY 7B')
if a in f8b:
    print ('FAMILY 8B')    




print('\nNow we are going to compare 2 elements by their eletronegavity \n ')

q = int(input('\n How many comparations ?\n' ))
for i in range(q):

    e1 = input('\nelemento 1\n')
    if e1 == 'F':
        e5 = 3.98
    if e1 == 'O':
        e5 = 3.44
    if e1 == 'Cl':
        e5 = 3.16
    if e1 == 'N':
        e5 = 3.04
    if e1 == 'Br':
        e5 = 2.96
    if e1 == 'I':
        e5 = 2.66
    if e1 == 'S':
        e5 = 2.58

    if e1 == 'Ac':
        e5 = 0.7
    if e1 == "La":
        e5 = 0.79
    if e1 == 'Sr':
        e5 = 0.82
    if e1 == 'Ce':
        e5 = 0.89
    if e1 == 'Th':
        e5 = 0.89
    if e1 == 'Na':
        e5 = 0.93
    if e1 == 'Y':
        e5 = 0.95

    if e1 == 'Li':
        e5 = 0.98
    if e1 == 'K':
        e5 = 0.82
    if e1 == 'Pr':
        e5 = 1.1
    if e1 == 'Pa':
        e5 = 1.1
    if e1 == 'Nd':
        e5 = 1.12
    if e1 == 'Pm':
        e5 = 1.13
    if e1 == 'Sm':
        e5 = 1.14

    if e1 == 'Gd':
        e5 = 1.17
    if e1 == "Dy":
        e5 = 1.2
    if e1 == 'Zr':
        e5 = 1.22
    if e1 == 'Er':
        e5 = 1.22
    if e1 == 'Tm':
        e5 = 1.23
    if e1 == 'Yb':
        e5 = 1.24
    if e1 == 'Lu':
        e5 = 1.25

    if e1 == 'Ta':
        e5 =  1.27
    if e1 == 'Cm':
        e5 = 1.28
    if e1 == 'W':
        e5 = 1.3
    if e1 == 'U':
        e5 = 1.3
    if e1 == 'Bk':
        e5 = 1.3
    if e1 == 'Cf':
        e5 = 1.3
    if e1 == 'Es':
        e5 = 1.3 
   
    if e1 == 'Fm':
        e5 = 1.3
    if e1 == 'Md':
        e5 = 1.3
    if e1 == 'No':
        e5 = 1.3
    if e1 == 'Lr':
        e5 = 1.3
    if e1 == 'Rf':
        e5 = 1.3
    if e1 == 'Db':
        e5 = 1.3
    if e1 == 'Mg':
        e5 = 1.31 
   




    if e1 == 'Nb':
        e5 = 1.31
    if e1 == 'Ca':
        e5 = 1.36
    if e1 == 'Am':
        e5 = 1.36
    if e1 == 'Pu':
        e5 = 1.38
    if e1 == 'Re':
        e5 = 1.5
    if e1 == 'Np':
        e5 = 1.5
    if e1 == 'Sc':
        e5 = 1.54
   



    if e1 == 'Cr':
        e5 = 1.55
    if e1 == 'Be':
        e5 = 1.57
    if e1 == 'Mo':
        e5 = 1.6
    if e1 == 'Al':
        e5 = 1.61
    if e1 == 'Bi':
        e5 = 1.62
    if e1 == 'Ti':
        e5 = 1.63
    if e1 == 'Cu':
        e5 = 1.65 
   


    if e1 == 'V':
        e5 = 1.66
    if e1 == 'ln':
        e5 = 1.69
    if e1 == 'Sn':
        e5 = 1.78
    if e1 == 'Zn':
        e5 = 1.81
    if e1 == 'Mn':
        e5 = 1.83
    if e1 == 'Fe':
        e5 = 1.88 
   
    if e1 == 'Si':
        e5 = 1.9
    if e1 == 'Ni':
        e5 = 1.9
    if e1 == 'Ru':
        e5 = 1.9
    if e1 == 'Ir':
        e5 = 1.9
    if e1 == 'Co':
        e5 = 1.91
    if e1 == 'Cd':
        e5 = 1.93
    if e1 == 'Sb':
        e5 = 1.96 
   

    if e1 == 'Pb':
        e5 = 2
    if e1 == 'Rn':
        e5 = 2
    if e1 == 'Ga':
        e5 = 2.01
    if e1 == 'At':
        e5 = 2.02
    if e1 == 'B':
        e5 = 2.04
    if e1 == 'I':
        e5 = 2.05
    if e1 == 'Xe':
        e5 = 2.1 
   

    if e1 == 'Tc':
        e5 = 2.16
    if e1 == 'As':
        e5 = 2.18
    if e1 == 'P':
        e5 = 2.19
    if e1 == 'H':
        e5 = 2.2
    if e1 == 'Rh':
        e5 = 2.26
    if e1 == 'Ag':
        e5 = 2.2
    if e1 == 'Pt':
        e5 = 2.2 
   





    if e1 == 'Au':
        e5 = 2.2
    if e1 == 'Fr':
        e5 = 2.24
    if e1 == 'Pd':
        e5 = 2.28
    if e1 == 'Hg':
        e5 = 2.28
    if e1 == 'Po':
        e5 = 2.33
    if e1 == 'Os':
        e5 = 2.36
    if e1 == 'TI':
        e5 = 2.54 
   


    if e1 == 'C':
        e5 = 2.55
    if e1 == 'Se':
        e5 = 2.55
    if e1 == 'S':
        e5 = 2.58
    if e1 == 'Ba':
        e5 = 2.6
    if e1 == 'Cs':
        e5 = 2.66
    if e1 == 'Kr':
        e5 = 2.96
 

    if e1 == 'Rb':
        e5 = 0.8


    e2 = input('\nelemento2\n')
    if e2 == 'F':
        e6 = 3.98
    if e2 == 'O':
        e6 = 3.44
    if e2 == 'Cl':
        e6 = 3.16
    if e2 == 'N':
        e6 = 3.04
    if e2 == 'Br':
        e6 = 2.96
    if e2 == 'I':
        e6 = 2.66
    if e2 == 'S':
        e6 = 2.58

    if e2 == 'Rb':
        e6 = 0.8


 
    if e2 == 'Ac':
        e6 = 0.7
    if e2 == "La":
        e6 = 0.79
    if e2 == 'Sr':
        e6 = 0.82
    if e2 == 'Ce':
        e6 = 0.89
    if e2 == 'Th':
        e6 = 0.89
    if e2 == 'Na':
        e6 = 0.93
    if e2 == 'Y':
        e6 = 0.95

    if e2 == 'Li':
        e6 = 0.98
    if e2 == 'K':
        e6 = 0.82
    if e2 == 'Pr':
        e6 = 1.1
    if e2 == 'Pa':
        e6 = 1.1
    if e2 == 'Nd':
        e6 = 1.12
    if e2 == 'Pm':
        e6 = 1.13
    if e2 == 'Sm':
        e6 = 1.14
    if e2 == 'Gd':
        e6 = 1.17
    if e2 == "Dy":
        e6 = 1.2
    if e2 == 'Zr':
        e6 = 1.22
    if e2 == 'Er':
        e6 = 1.22
    if e2 == 'Tm':
        e6 = 1.23
    if e2 == 'Yb':
        e6 = 1.24
    if e2 == 'Lu':
        e6 = 1.25

    if e2 == 'Ta':
        e6 =  1.27
    if e2 == 'Cm':
        e6 = 1.28
    if e2 == 'W':
        e6 = 1.3
    if e2 == 'U':
        e6 = 1.3
    if e2 == 'Bk':
        e6 = 1.3
    if e2 == 'Cf':
        e6 = 1.3
    if e2 == 'Es':
        e6 = 1.3 
   
    if e2 == 'Fm':
        e6 = 1.3
    if e2 == 'Md':
        e6 = 1.3
    if e2 == 'No':
        e6 = 1.3
    if e2 == 'Lr':
        e6 = 1.3
    if e2 == 'Rf':
        e6 = 1.3
    if e2 == 'Db':
        e6 = 1.3
    if e2 == 'Mg':
        e6 = 1.31 
   




    if e2 == 'Nb':
        e6 = 1.31
    if e2 == 'Ca':
        e6 = 1.36
    if e2 == 'Am':
        e6 = 1.36
    if e2 == 'Pu':
        e6 = 1.38
    if e2 == 'Re':
        e6 = 1.5
    if e2 == 'Np':
        e6 = 1.5
    if e2 == 'Sc':
        e6 = 1.54
   



    if e2 == 'Cr':
        e6 = 1.55
    if e2 == 'Be':
        e6 = 1.57
    if e2 == 'Mo':
        e6 = 1.6
    if e2 == 'Al':
        e6 = 1.61
    if e2 == 'Bi':
        e6 = 1.62
    if e2 == 'Ti':
        e6 = 1.63
    if e2 == 'Cu':
        e6 = 1.65 
   


    if e2 == 'V':
        e6 = 1.66
    if e2 == 'ln':
        e6 = 1.69
    if e2 == 'Sn':
        e6 = 1.78
    if e2 == 'Zn':
        e6 = 1.81
    if e2 == 'Mn':
        e6 = 1.83
    if e2 == 'Fe':
        e6 = 1.88 
   
    if e2 == 'Si':
        e6 = 1.9
    if e2 == 'Ni':
        e6 = 1.9
    if e2 == 'Ru':
        e6 = 1.9
    if e2 == 'Ir':
        e6 = 1.9
    if e2 == 'Co':
        e6 = 1.91
    if e2 == 'Cd':
        e6 = 1.93
    if e2 == 'Sb':
        e6 = 1.96 
   

    if e2 == 'Pb':
        e6 = 2
    if e2 == 'Rn':
        e6 = 2
    if e2 == 'Ga':
        e6 = 2.01
    if e2 == 'At':
        e6 = 2.02
    if e2 == 'B':
        e6 = 2.04
    if e2 == 'I':
        e6 = 2.05
    if e2 == 'Xe':
        e6 = 2.1 
   

    if e2 == 'Tc':
        e6 = 2.16
    if e2 == 'As':
        e6 = 2.18
    if e2 == 'P':
        e6 = 2.19
    if e2 == 'H':
        e6 = 2.2
    if e2 == 'Rh':
        e6 = 2.26
    if e2 == 'Ag':
        e6 = 2.2
    if e2 == 'Pt':
        e6 = 2.2 
   





    if e2 == 'Au':
        e6 = 2.2
    if e2 == 'Fr':
        e6 = 2.24
    if e2 == 'Pd':
        e6 = 2.28
    if e2 == 'Hg':
        e6 = 2.28
    if e2 == 'Po':
        e6 = 2.33
    if e2 == 'Os':
        e6 = 2.36
    if e2 == 'TI':
        e6 = 2.54 
   


    if e2 == 'C':
        e6 = 2.55
    if e2 == 'Se':
        e6 = 2.55
    if e2 == 'S':
        e6 = 2.58
    if e2 == 'Ba':
        e6 = 2.6
    if e2 == 'Cs':
        e6 = 2.66
    if e2 == 'Kr':
        e6 = 2.96
   



    if e5 > e6:
        print(e1,'its more eletronegative ')
  
    
    if e5==e6:
        print('equal')

    if e6 > e5:
        print(e2,'its more eletronegative ')

print('!source : https://www.lenntech.com/periodic/elements/rb.htm' )
