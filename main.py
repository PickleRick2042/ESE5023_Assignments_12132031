import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename="C:/Users/ASUS/PycharmProjects/usgs_earthquakes.csv"
date=csv.Dateset(filename)
for i in date.variables.keys():
    lat=date.variables["Dimension"].squeeze()
    lon=date.variables["longitude "].squeeze()
    u=date.variables["year"].squeeze()
    idate=date.variables["magnitude"].squeeze()

    m = Basemap(resolution='l', area_thresh=10000, projection='cyl', llcrnrlon=50, urcrnrlon=150, llcrnrlat=0,
                urcrnrlat=70)
    fig1 = plt.figure()
    ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    x, y = m(lon, lat)
    m.drawparallels(np.arange(0, 70, 10.), labels=[1, 1, 0, 0], fontsize=15)
    m.drawmeridians(np.arange(50, 150, 20), labels=[0, 0, 0, 1], fontsize=15)
    CS2 = m.contourf(x, y, u[0, :, :])
    m.colorbar(CS2)
    m.drawcoastlines(linewidth=0.2)
    plt.title('U', size=20)

    plt.show()
    import numpy as np

    import netCDF4 as nc

    import matplotlib.pyplot as plt

    from mpl_toolkits.mplot3d import Axes3D

    file_path = "C:\\data_yh\\2019.4.1-2020.4.1.nc"

    file = nc.Dataset(file_path)

    time = (file.variables['time'][:])

    sla = (file.variables['sla'][:])

    lat = (file.variables['latitude'][:])

    lon = (file.variables['longitude'][:])

    data_lon = np.array(lon)

    data_lat = np.array(lat)

    data_time = np.array(time)

    data_sla = np.array(sla)


