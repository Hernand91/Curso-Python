#creando una lista (se puede modificar)
lista = ["Hernan Devoto","Soy Hernan",True,1.65]

#creando una tupla (no se puede modificar)
tupla = ("Hernan Devoto","Soy Hernan",True,1.64)

#esto rs valido
lista[3] ="Maquinola"

#esto no
#tupla[3] = maquinola

print(lista[3])



#creando un conjunto (set) (no se accede al elemento por indice, no almacena datos duplicados) 
conjuto = {"Hernan Devoto","Soy Hernan",True,1.65,"Soy Hernan"}

#print(conjunto[3])  no se puede acceder al elemento

#creando un diccionario (dict) (la estructura es key: value y lo separamos con comas)
diccionario = {
    "nombre" : "Hernan Devoto",
    "canal" : "Soy Hernan", 
    "esta_emocionado" : True,
    "altura" : 1.65,
    "dato_duplicado" : "Soy Hernan"
}

print(diccionario["altura"])
