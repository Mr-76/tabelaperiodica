

#class Elemento():
 #   def __init__(self,massa,atomico,eletrong,estado,tipo):
  #      self.massa = massa
   #     self.atomico = atomico
    #    self.eletrong = eletrong
     #   self.estado = estado
       # self.tipo = tipo 

eletro = {'fe':3.0}
atomico = {'fe':26}
massa = {'fe':55.8}
estado = {'fe':'solido'}
tipo = {'fe':'normal'}

class Elemento():
    def __init__(self,nome):
        self.massa = massa[nome]
        self.atomico = atomico[nome]
        self.eletrong = eletro[nome]
        self.estado = estado[nome]
        self.tipo = tipo[nome]

FERRO = Elemento('fe')

print(FERRO.massa,FERRO.eletrong,FERRO.estado,FERRO.tipo,FERRO.atomico)


 
