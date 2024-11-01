import csv

''' with open("./WEEK7/random_lat_lon_data.csv", "r") as f:
    
    reader = csv.reader(f)
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        
        print(lat, long)
        print(lat+long)
'''
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(28.689108, 77.786714, 16)
gmap.coloricon = "http://www.googlemapsmakers.com/v1/%s/"

with open("./WEEK7/random_lat_lon_data.csv") as f:
    reader = csv.reader(f)
    k = 0
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        
        if(k==0):
            gmap.marker(lat,long, 'green')
            k = 1
        else:
            gmap.marker(lat,long, 'blue')
            
gmap.marker(lat, long, 'red')

gmap.draw("mymap.html")