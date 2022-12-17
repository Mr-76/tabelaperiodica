# -*- coding: utf-8 -*-

import numpy as np
import dicionario


def encontra_elemento(elemento):
    tabela = np.array([['H', '', '', '', '', '', '', '', '', '', '', '', 'B', 'C', 'N', 'O', 'F', 'NE'], ['LI', 'BE', '', '', '', '', '', '', '', '', '', '', 'B', 'C', 'N', 'O', 'F', 'NE'], ['NA', 'MG', '', '', '', '', '', '', '', '', '', '', 'AL', 'SI', 'P', 'S', 'CL', 'AR'], ['K', 'CA', 'SC', 'TI', 'V', 'CE', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR'], [
                      'RB', 'SR', 'Y', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'LN', 'SN', 'SB', 'TE', 'L', 'XE'], ['CS', 'BA', 'MUITO1', 'HF', 'TA', 'W', 'RE', 'OS', 'LR', 'PT', 'AU', 'HG', 'TI', 'PB', 'BI', 'PO', 'AT', 'RN'], ['FR', 'RA', 'MUITO2', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT', 'DS', 'RG', 'CN', 'NH', 'FL', 'MC', 'LV', 'TS', 'OG']])

    MUITO1 = ['LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU',
              'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU']
    MUITO2 = ['AC', 'TH', 'PA', 'U', 'NP', 'PU', 'AM',
              'CM', 'BK', 'CF', 'ES', 'FM', 'MD', 'NO', 'LR']

    familiaB = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # so precisa familia B

    familia = ''
    familia_periodo = ''
    Localizando_o_elemento = np.where(tabela == elemento)

    (linha, coluna) = Localizando_o_elemento

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

    familia_periodo = ("Elemento pertence a familia {}{} de periodo {}".format(
        int(coluna+1), familia, int(linha+1)))

    print(familia_periodo)

    return familia_periodo


print("<<<<<<<<<<<<<<<<<<<<<<Periodic table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("H\nLi", "Be                              B  C  N  O  F  Ne\nNa", "Mg                              Al Si P  S  Cl Ar\nK", " Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr\nRb",
      "Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe\nCs", "Ba   Hf Ta W  Re Os Ir Pt Au Hg Ti Pb Bi Po At Rn\nFr", "Ra   Rf Db Sg Bh Hs Mt Ds Rg Cn Nh FI Mc Lv Ts Og")
print("_____________________________________________________\n")


elemento = input("qual elemento? ")

# encontra_elemento(elemento)

"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!-----proximo passo deletar linha de cod , e substituir metodo de achar eletrons etc os valores----- !!!!!!!!!!!!!"


Dic_eletro = dicionario.elementos_eletro


while True:
    elemento = input("Escolha o elemento \ncaso queira parar digite PARE\n")
    if elemento == "PARE":
        break
    else:
        for i in Dic_eletro:
            if i.lower() == elemento.lower():
                print(Dic_eletro[i])
                print("found")


print('!source : https://www.lenntech.com/periodic/elements/rb.htm')
