#kylah kerr
#13 April 2022
#leaves a marker on folium map

import folium
import pandas as pd

infile = input("Enter inflie: ")
outfile = input("Enter outfile: ")

Nyc = pd.read_csv(infile)
mapNyc = foluim.Map(location=[40.75, -74.125])

folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapNYC)

mpaNyc.save(outfile='nycMap.html')
