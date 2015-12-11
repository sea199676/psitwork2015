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
#Labels use in northeastern of thailand
labels = ['NakhonRatchasima', 'BuriRam', 'Surin', 'SiSaKet',\
'UbonRatchathani', 'Yasothon', 'Chaiyaphum', 'AmnatCharoen', 'Bungkan', 'NongBuaLamPhu', 'KhonKaen',\
'UdonThani', 'Loei', 'NongKhai', 'MahaSarakham', 'RoiEt', 'Kalasin', 'SakonNakhon', 'NakhonPhanom', 'Mukdahan']
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
 
lon = [102.10, 103.10, 103.49, 104.32, 104.85, 104.13, 102.03, 104.62, 103.27, 102.38, 102.83, 102.75, 101.71, 102.74, 103.30, 103.65, 103.50, 104.14, 104.78, 104.72]
lat = [14.97, 15.00, 14.88, 15.12, 15.22, 15.80, 15.80, 15.86, 18.23, 17.16, 16.43, 17.41, 17.48, 17.86, 16.18, 16.05, 16.43, 17.15, 17.40, 16.54]



for label, xpt, ypt in zip(labels, lon, lat):
        print(label)
        x, y = my_map(xpt, ypt)
        color_point = make_color(label, keep_debt)
        my_map.plot(x, y, color_point, markersize=8)
        ptl.text(x, y, label)

ptl.show()

##http://introtopython.org/visualization_earthquakes.html
