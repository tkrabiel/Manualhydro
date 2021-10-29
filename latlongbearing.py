import math
'''This script lets you know the final LAT LONG given an innitial LAT LONG and a bearing and a distance.
 It also calulates the radius of the earth based on the LAT given to it. 
 Your bearing needs to be degrees and will be converted and your lat and long need to be in decimills degrees
  36.8559	76.2938
'''
#put all your starting data here
lat1 = math.radians(36.8559) #Current lat point converted to radians
lon1 = math.radians(76.2938) #Current long point converted to radians
d = 1.7949 #Distance in cm on paper
scale = 1500
brng = 351 #your bearing in DEGREES it will be converted latter

d = (d*scale)/100000

print (d)

#finds the radius of the earth at the lat given I left the radius DEF
#as a long string so I can debug and see what the outputs are at each step
# simply put a print stament below each to see
def radius (lat1):
    B = (lat1) #converting into radians
    a = 6378.137 #Radius at sea level at equator
    b = 6356.752 #Radius at poles
    aWGS = 6378.137  #Radius at sea level at equator
    bwgs = 6356.7523142   #Radius at poles
    c = (aWGS**2*math.cos(B))**2
    d = (bwgs**2*math.sin(B))**2
    e = (aWGS*math.cos(B))**2
    f = (bwgs*math.sin(B))**2
    R = math.sqrt((c+d)/(e+f))
    #print (R)
    return R
R = float(radius(lat1))
print (R ,"km")
brng = math.radians(brng) #Bearing is degrees

#the math for the lat1 and lon1 to LAT2 and LON2
lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
     math.cos(lat1)*math.sin(d/R)*math.cos(brng))

lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
             math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

lat2 = math.degrees(lat2)
lon2 = math.degrees(lon2)

lat2 = str(lat2)

lat2degree = int(lat2 [0:2])

lat2min = float(lat2)

lat2min = float(-1*(lat2degree-lat2min)*60)

lon2 = str(lon2)

lon2degree = int(lon2 [0:2])

lon2min = float(lon2)

lon2min = float(-1*(lon2degree-lon2min)*60)

print (lat2,lon2)

print ("LAT",str(lat2degree) + "D" + str(lat2min) +"N", "LONG",str(lon2degree) + "D" + str(lon2min)+"W")