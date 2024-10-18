import justpy as Jp

def app():
    wp = Jp.QuasarPage()
    h1 = Jp.QDiv(a=wp, text = "no se que dice el original",classes="text-h2 text-center q-pa-lg")
    p1 = Jp.QDiv(a=wp, text = "curso de analisis y no se  uqe mas")
    return wp

Jp.justpy(app)