import folium
import pandas

data = pandas.read_csv("universities.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])


map=folium.Map(location =[42.3394998755698, -71.08892085506822],zoom_start=6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Universities")

for lt,ln,na in zip(lat,lon,name):
    fgv.add_child(folium.Marker(location = [lt,ln],popup = str(na), icon = folium.Icon(color='red')))

map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("map1.html")
