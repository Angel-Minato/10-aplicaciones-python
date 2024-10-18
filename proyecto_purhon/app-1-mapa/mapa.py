import folium
import pandas
import cv2

def colorear(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev <3000:
        return 'orange'
    else:
        return 'red'

dt = pandas.read_csv("Volcanoes.txt")
Cord = list(zip(dt["LAT"], dt["LON"]))
eleva = list(dt["ELEV"])
name = list(dt["NAME"])

html = """<h4>Volcan informacion:</h4>
Nombre:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Altura: %s m
"""

coordenadas = [
    [24.035310, -104.657519],  
    [24.040000, -104.660000],  
    [24.045000, -104.665000],  
    [24.050000, -104.670000],  
    [24.055000, -104.675000]   
]

map = folium.Map(
    location=[24.035310, -104.657519],
    zoom_start=6,
    tiles="OpenStreetMap",
   
)

fg = folium.FeatureGroup(name="VOLCANES")

for i, elt, name in zip(Cord,eleva,name):
    texto = folium.IFrame(html=html %(name, name, elt), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=i, radius = 8, popup= folium.Popup(texto,parse_html=True),fill_color= colorear(elt),color='grey',fill_opacity=0.7))

with open('world.json', 'r', encoding='utf-8-sig') as f:
    dtj = f.read()

fgd = folium.FeatureGroup(name="Poblacion")

fgd.add_child(folium.GeoJson(data=dtj,style_function=lambda x: {
                                 'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
                                 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
                                 else 'red'
                             }))
#fg.add_child(folium.GeoJson(dt=(open('world.json', 'r',  encoding='utf-8-sig').read())))

map.add_child(fg)
map.add_child(fgd)
map.add_child(folium.LayerControl())

map.save("Mapa.html")
