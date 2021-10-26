1#earthquake
import pandas as pd
import numpy as np
data=pd.read_csv("D:/earthquake/earthquakes-2021-10-23_11-40-03_+0800.tsv",encoding="gbk",sep="\t")
T1=data.groupby(["Country"])["Deaths"].sum()
sorted(T1)
print(T1[0:9])
mag=data["Mag"]
time=data["Year"]
if mag>6:
 print(time)
#Wind speed in Shenzhen during the past 10 years
import pandas as pd
import numpy as np
data2=pd.read_csv("C:/Users/ASUS/PycharmProjects/Wind speed in Shenzhen during the past 10 years.csv")
print(data2.loc[:["DATE",'WIND']])
#3. Explore a data set
import pandas as pd
import numpy as np
data3=pd.read_csv("C:/Users/ASUS/PycharmProjects/Wind speed in Shenzhen during the past 10 years.csv")
print(data3.loc[:['DATE','TMP']])

