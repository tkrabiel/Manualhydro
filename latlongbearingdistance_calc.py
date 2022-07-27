import math
'''This script lets you know the final LAT LONG given an innitial LAT LONG and a bearing and a distance.
 It also calulates the radius of the earth based on the LAT given to it. 
 Your bearing needs to be degrees and will be converted and your lat and long need to be in decimills degrees
  36.8559	76.2938
'''


#finds the radius of the earth at the lat given I left the radius DEF
#as a long string so I can debug and see what the outputs are at each step
# simply put a print stament below each to see
def radius (lat1):
    B = (lat1) #converting into radians
    #a = 6378.137 #Radius at sea level at equator
    #b = 6356.752 #Radius at poles
    aWGS = 6378.137  #Radius at sea level at equator
    bwgs = 6356.7523142   #Radius at poles
    c = (aWGS**2*math.cos(B))**2
    d = (bwgs**2*math.sin(B))**2
    e = (aWGS*math.cos(B))**2
    f = (bwgs*math.sin(B))**2
    R = math.sqrt((c+d)/(e+f)) #return the radius in KM!!!
    #print (R)
    return R

def secondcord(lat1,lon1, R, d,brng): #must be in radians
#the math for the lat1 and lon1 to LAT2 and LON2 retun lat2 long2 as radian
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) + math.cos(lat1)*math.sin(d/R)*math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    #lat2 = math.degrees(lat2)
    #lon2 = math.degrees(lon2)
    return(lat2,lon2)

# math for calculating the bearing between a lat long to lat long
#return a float
def true_bearing(longa,lata,longb,latb):
    Ldiff = abs(longa - longb)
    x = math.cos(latb)*math.sin(Ldiff)
    y = math.cos(lata)*math.sin(latb)-math.sin(lata)*math.cos(latb)*math.cos(Ldiff)
    #x = math.cos(math.radians(latb) * math.sin(Ldiff))
    #y = math.cos(math.radians(lata) * math.sin(math.radians(latb) - math.sin(math.radians(lata) * math.cos(math.radians(latb) * math.cos(Ldiff)))))
    brg = math.atan2(x,y) #returns radians
    return brg





def distance(lat1,lon1, lat2, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    # Haversine formula

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2

    c = 2 * math.asin(math.sqrt(a))

    # Radius of earth in kilometers.
    r = radius(lat1)

    # calculate the result in KM!!!
    return float(c * r)