import netCDF4
import numpy as np
from matplotlib import pyplot as plt

ncfile = netCDF4.Dataset('ascat_20211103_011500_metopa_78044_eps_o_coa_3202_ovw.l2.nc')
koordinats = [18,13,16,2]
latvar = ncfile['lat'][:]
lonvar = ncfile['lon'][:]
wind = ncfile['wind_speed'][:]

def naive_fast(latvar,lonvar,lat0,lon0):
    latvals = latvar[:]
    lonvals = lonvar[:]
    ny,nx = latvals.shape
    dist_sq = (latvals-lat0)**2 + (lonvals-lon0)**2
    minindex_flattened = dist_sq.argmin()
    iy_min,ix_min = np.unravel_index(minindex_flattened, latvals.shape)
    return iy_min,ix_min

shagi = 10
lonp = (koordinats[0]-koordinats[2])/shagi
latp = (koordinats[1]-koordinats[3])/shagi
koor = [koordinats[0],koordinats[1],koordinats[0]-lonp,koordinats[1]-latp,koordinats[0]-lonp*2,koordinats[1]-latp*2,koordinats[0]-lonp*3,koordinats[1]-latp*3,koordinats[0]-lonp*4,koordinats[1]-latp*4,koordinats[0]-lonp*5,koordinats[1]-latp*5,koordinats[0]-lonp*6,koordinats[1]-latp*6,koordinats[0]-lonp*7,koordinats[1]-latp*7,koordinats[0]-lonp*8,koordinats[1]-latp*8,koordinats[0]-lonp*9,koordinats[1]-latp*9,koordinats[0]-lonp*10,koordinats[1]-latp*10]
punkt = []
wind_speed = []
x = 0
while x <= shagi:
  lon = koor[x]
  lat = koor[x+1]
  iy,ix = naive_fast(latvar, lonvar, lon, lat) 
  wind_speed.append(wind[iy,ix])
  punkt.append(x)
  x += 1

plt.plot(punkt,wind_speed,'r-.')
plt.title("Разрез поля скорости ветра", fontsize=20)
plt.xlabel ("Пункты")
plt.ylabel ("Скорость ветра")
plt.text(punkt[0],wind_speed[0],str(wind_speed[0])+'м/с')
plt.text(punkt[1],wind_speed[1],str(wind_speed[1])+'м/с')
plt.text(punkt[2],wind_speed[2],str(wind_speed[2])+'м/с')
plt.text(punkt[3],wind_speed[3],str(wind_speed[3])+'м/с')
plt.text(punkt[4],wind_speed[4],str(wind_speed[4])+'м/с')
plt.text(punkt[5],wind_speed[5],str(wind_speed[5])+'м/с')
plt.text(punkt[6],wind_speed[6],str(wind_speed[6])+'м/с')
plt.text(punkt[7],wind_speed[7],str(wind_speed[7])+'м/с')
plt.text(punkt[8],wind_speed[8],str(wind_speed[8])+'м/с')
plt.text(punkt[9],wind_speed[9],str(wind_speed[9])+'м/с')
plt.text(punkt[10],wind_speed[10],str(wind_speed[10])+'м/с')
plt.show()   
