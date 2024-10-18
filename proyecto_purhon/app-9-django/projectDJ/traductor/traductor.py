from googletrans import Translator

def traducir(text):
    traducion = Translator()
    tr = traducion.translate(text=text, dest='de')
    return tr.text