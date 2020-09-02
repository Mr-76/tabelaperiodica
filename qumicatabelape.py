import familiyastestedeimport
f1a=('Li', 'Na', 'K', 'Rb', 'Cs', 'Fr')
f2a=('Be', 'Ca', 'Mg', 'Sr', 'Ba','Ra')
f3a=('B', 'Al', 'Ga', 'In', 'Tl')
f4a=('C', 'Si', 'Ge', 'Sn', 'Pb')
f5a=('N', 'P', 'As', 'Sb', 'Bi')
f6a=('O', 'S', 'Se', 'Te', 'Po')
f7a=('F', 'Cl', 'Br', 'I', 'At')
f8a=('He', 'Ne', 'Ar', 'Kr' , 'Xe', 'Rn')

a=input('enter value')




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
else:
    print('family B')





print('F',
'O',
'Cl',
'N',
'Br',
'I',
'S',
'C',
'Metaisnobres',
'H',
'P',
'Semimetais' 
,'Metaiscomuns',
'Fr')







q = int(input('quantas comparaçoes?' ))
for i in range(q):

    e1 = input('elemento 1')
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


    e2 = input('elemento2')
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


    
    if e5 > e6:
        print(e1,' eh mais eletro negativo')
  
    
    if e5==e6:
        print('iguais')

    elif e6> e5:
        print(e2,' eh maiseletronegativo')

