from MASSA import massa

eletro = {'F':3.0}
estado = {'F':'solido'}
tipo = {'F':'normal'}

class Elemento():
    def __init__(self,nome):
        self.massa = massa[nome]
       # se#lf.atomico = atomico[nome]
        self.eletrong = eletro[nome]
        self.estado = estado[nome]
        self.tipo = tipo[nome]

FERRO = Elemento('F')

print(FERRO.massa,FERRO.eletrong,FERRO.estado,FERRO.tipo)


 
