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
labels = ['NakhonSiThammarat','Krabi','Phangnga','Phuket','SuratThani','Ranong','Chumphon','Songkhla','Satun','Trang','Phattalung','Pattani','Yala','Narathiwat']
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
 
lon = [99.96, 98.91, 98.51, 98.39, 99.19, 98.63, 99.17, 100.59, 100.06, 99.61, 100.07, 101.25, 101.28, 101.82]
lat = [8.43, 8.05, 8.43, 7.89, 9.8, 9.96, 10.49, 7.20, 6.62, 7.55, 7.61, 6.86, 6.54, 6.42]



for label, xpt, ypt in zip(labels, lon, lat):
        print(label)
        x, y = my_map(xpt, ypt)
        color_point = make_color(label, keep_debt)
        my_map.plot(x, y, color_point, markersize=8)
        ptl.text(x, y, label)

ptl.show()

##http://introtopython.org/visualization_earthquakes.html
