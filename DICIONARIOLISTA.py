
elementos_eletro = {'F':3.98,"O":3.44,"Cl":3.16,'N':3.04,'Br':2.96,'I':2.66,'S':2.58,'Ac':0.7,"La":0.79,'Sr':0.82,'Ce':0.89,'Th':0.89,'Na':0.93,'Y':0.95,
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





Dicionario_para_lista = list(elementos_eletro.items())#transformando a lista de tuplas objeto do dicionario em uma lista 'real'


print(Dicionario_para_lista)

tipos = ("massa","atomico","estado","radio")
#massa
for tipo in tipos:
    print("tipo: {}".format(tipo))
    
    escolha = input("esse e o tipo para editar ? Y/N" )

    if escolha == "N":
        continue #pular para outro tipo 
    if escolha == "Y":
        Nome_Arquivo = ("{}.txt".format(tipo))
"""
    with open(Nome_Arquivo,"r") as arquivo_deTexto:
        texto = arquivo_deTexto.readlines()
        print(texto)
"""
    try:
        with open(Nome_Arquivo,"r") as arquivo_deTexto:
            texto = arquivo_deTexto.readlines()
       
        convertendo_ParaDict = ast.literal_eval(texto[0])
        lista_Tuplas = list(convertendo_ParaDict.items())
        
        adicionar_ou_modificar = input('deseja adicionar ou modificar? A/M')
        
        if adicionar_ou_modificar == "M":
            contador = -1
            qual_elemento = input("Coloque aquie o nome do elemento ") 

        for item in  lista_Tuplas: #procurando elemento na lista               
            contador += 1 #index
            if item[0] == qual_elemento: #item  se refere ao primeiro elemento da tupla (key , valor)
                break

        print(contador) # me da o indice


        print(lista_Tuplas[contador]) #me da o elemento 

        valor = int(input("valor a modificar susbstituir no elemento? "))
        lista_Tuplas[contador] #modificar para indice
        lista_tupla = []
        lista_tupla.append(lista_Tuplas[contador][0])
        lista_tupla.append(valor)

        lista_Tuplas[contador] = tuple(lista_tupla)

        dicionario_volta = dict(lista_Tuplas)

        
        with open(Nome_Arquivo,'w') as arquivo_deTexto:
            string = str(dicionario_volta)
            arquivo_deTexto.write(string)

        if adicionar_ou_modificar == "A":
            with open(Nome_Arquivo,r) as arquivo_deTexto:
                texto = arquivo_deTexto.readlines()

            convertendo_ParaDict = ast.literal_eval(texto[0])
            lista_Tuplas = list(convertendo_ParaDict.items())

            elementoTupla,valorTupla = input("digite o elemento e o valor entre espacos ex: Fe 2").split()

            listaElemento = [elementoTupla,int(valorTupla)]

            lista_Tuplas.append(tuple(listaElemento))

            dicionario_volta = dict(lista_Tuplas)

            with open(Nome_Arquivo,'w') as arquivo_deTexto:
                string = str(dicionario_volta)
                arquivo_deTexto.write(dicionario_volta)
    except:
        print("criando arquivo")
        
        for index_tupla in range(len(Dicionario_para_lista)):
            
            quitar = input('quitear programa ? S/N ')
            if quitar == "S":
                break

            else:
                lista_tuplas = []
                print("elemento ",Dicionario_para_lista[index_tupla][0])
                valor = input("digite o valor a ser modificado no elemento ")
                lista_tuplas.append(Dicionario_para_lista[index_tupla][0])
                lista_tuplas.append(valor) 
                Dicionario_para_lista[index_tupla] = tuple(lista_tuplas)
                dicionario_volta = dict(Dicionario_para_lista)
                with open(Nome_Arquivo,'w') as arquivo_deTexto:
                    string = str(dicionario_volta)
                    arquivo_deTexto.write(string)
 