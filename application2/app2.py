import folium, numpy, json
import pandas as pd

df = pd.read_csv('Volcanoes_USA.txt',sep=',')
lat = list(df['LAT'])
lon = list(df['LON'])
elev = list(df['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 < elevation < 3000:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='My Map')

for lt,ln,el in zip(lat,lon,elev): # Note the zip function
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el),fill_color=color_producer(el),color='grey',fill_opacity=0.7,fill=True))

fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))

map.add_child(fg)

map.save('master_map.html') # converts it to web language
