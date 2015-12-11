from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as ptl
import numpy as np
import csv
def make_color(label, keep_debt):
        print(keep_debt[label])
        if int(keep_debt[label]) >= 300000:
                return "ro"
        elif int(keep_debt[label]) >= 200000:
                return "yo"
        elif int(keep_debt[label]) >= 100000:
                return "go"
        elif int(keep_debt[label]) >= 50000:
                return "bo"
        else:
                return "wo"


years = int(input())
name_file = "data%d.txt"%years
file=open(name_file, 'rt')
data=csv.reader(file)
table=[row for row in data]
keep_debt = {}
#Labels use in north of thailand
labels = ['Bangkok' ,'SamutPrakan' ,'Nonthaburi' ,'PathumThani' ,'PhraNakhonSiAyutthaya' ,'AngThong' ,'LopBuri' ,'SingBuri', 'ChaiNat' ,'Saraburi' ,'ChonBuri' ,'Rayong' ,'Chanthaburi' ,'Trat'
,'Chachoengsao' ,'PrachinBuri' ,'NakhonNayok' ,'SaKaeo' ,'Ratchaburi' ,'Kanchanaburi' ,'SuphanBuri' ,'NakhonPathom' ,'SamutSakhon' ,'SamutSongkhram' ,'Phetchaburi', 'PrachuapKhiriKhan']
for i in table:
        if i[0] in labels:
                keep_debt[i[0]] = i[3]

# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
my_map = Basemap(projection='merc', lat_0=15, lon_0=100,
    resolution = 'h', area_thresh = 0.5,
    llcrnrlon=90, llcrnrlat=0.25,
    urcrnrlon=120, urcrnrlat=21.5)
 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()
 
lon = [100.50, 100.60, 100.51, 100.52, 100.55, 100.45, 100.12, 100.65, 100.14, 100.91, 100.98, 101.43, 102.10, 102.24, 102.51, 101.22, 102.06, 99.81, 99.53, 100.11, 100.06, 100.27, 100.00, 99.94, 99.8]
lat = [13.75, 13.60, 13.86, 14.02, 14.34, 14.58, 15.19, 14.79, 15.12, 14.52, 13.36, 12.83, 12.61, 12.24, 14.05, 14.20, 13.82, 13.52, 14.02, 14.47, 13.81, 13.54, 13.40, 13.11, 11.81]



for label, xpt, ypt in zip(labels, lon, lat):
        print(label)
        x, y = my_map(xpt, ypt)
        color_point = make_color(label, keep_debt)
        my_map.plot(x, y, color_point, markersize=8)
        ptl.text(x, y, label)

ptl.show()

##http://introtopython.org/visualization_earthquakes.html
