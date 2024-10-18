import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def traducir(palabra):
    palabra = palabra.lower()  
    if palabra in data:
        return data[palabra] 
    elif palabra.title() in data:  
        return data[palabra.title()]  
    elif len(get_close_matches(palabra, data.keys())) > 0: 
        yn = input("¿Quisiste decir %s en su lugar? Ingresa Y si sí, o N si no: " % get_close_matches(palabra, data.keys())[0])
        if yn == "Y": 
            return data[get_close_matches(palabra, data.keys())[0]]  
        elif yn == "N":  
            return "La palabra no existe. Por favor, verifica nuevamente."
        else:  
            return "No entendimos tu entrada."
    else:
        return "La palabra no existe. Por favor, verifica nuevamente."

palabra = input("Ingresa una palabra: ")
resultado = traducir(palabra)

if type(resultado) == list:
    for item in resultado:
        print(item)
else:
    print(resultado)  
