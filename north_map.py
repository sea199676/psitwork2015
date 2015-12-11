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
labels = ['Lamphun', 'ChiangMai', 'Lampang', 'Uttaradit', 'Phrae', 'Nan', 'Phayao', 'ChiangRai', 'MaeHongSon',\
          'NakhonSawan', 'UthaiThani', 'KamphaengPhet', 'Tak', 'Sukhothai', 'Phitsanulok', 'Phichit', 'Phetchabun']
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
 
lon = [99, 98.59, 99.30, 102.46, 100.09, 100.77, 99.55, 99.50, 98.43, 100.12, 100.02, 99.30, 99.8, 99.72, 100.26, 100.22, 101.08]
lat = [18, 18.47, 18.18, 17.36, 18.07, 18.77, 19.11, 19.52, 19.36, 15.35, 15.69, 16.28, 16.52, 17.24, 16.82, 16.26, 16.25]



for label, xpt, ypt in zip(labels, lon, lat):
        print(label)
        x, y = my_map(xpt, ypt)
        color_point = make_color(label, keep_debt)
        my_map.plot(x, y, color_point, markersize=8)
        ptl.text(x, y, label)

ptl.show()

##http://introtopython.org/visualization_earthquakes.html
