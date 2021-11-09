filename="C:/Users/ASUS/PycharmProjects/NOAA_NCDC_ERSST_v3b_SST.nc"
date=nc.Dateset(filename)
for i in date.variables.keys():
    lat=date.variables["year"].squeeze()
    lon=date.variables["tempature"].squeeze()
    u=date.variables["hang"].squeeze()
    idate=date.variables["lie"].squeeze()

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
    import xarray as xr

    file_path = "C:/Users/ASUS/PycharmProjects/CERES_EBAF-TOA_200003-201701.nc"

    file = nc.Dataset(file_path)

    time = (file.variables['time'][:])

    sla = (file.variables['sla'][:])

    lat = (file.variables['latitude'][:])

    lon = (file.variables['longitude'][:])

    data_lon = np.array(lon)

    data_lat = np.array(lat)

    data_time = np.array(time)

    data_sla = np.array(sla)

    print(len(data_sla))

    print(len(time))

    print(len(lat))

    print(len(lon))

    data_plt_sla = data_sla[0, :, :]


    def find_max(data_matrix):


    new_data = []

    for i in range(len(data_matrix)):

    new_data.append(max(data_matrix[i]))

    print("data_matrix最大值为", max(new_data))


    def find_min(data_matrix):


    new_data = []

    for i in range(len(data_matrix)):

    new_data.append(min(data_matrix[i]))

    print(min(new_data))

    print(max(data_lat))

    print(max(data_lon))

    print(min(data_lon))

    print(min(data_lat))

    print(find_max(data_plt_sla))

    fig = plt.figure()

    X = data_lon

    Y = data_lat

    X, Y = np.meshgrid(X, Y)

    ax2.contour(X, Y, data_plt_sla, zdir='z', offset=-3, cmap="longwave")

    ax2.contourf(X, Y, data_plt_sla, zdir='z', offset=-3, cmap="longwave")
    ax3.contour(X, Y, data_plt_sla, zdir='z', offset=-3, cmap="shortwave")

    ax3.contourf(X, Y, data_plt_sla, zdir='z', offset=-3, cmap="shortwave")
    plt.show()

