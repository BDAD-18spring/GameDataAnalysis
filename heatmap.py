import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from pyspark.sql import SparkSession

import pandas as pd
import pydoop.hdfs as hd

# create a spark session
#sparkSession = SparkSession.builder.master("local").appName("draw heat map").getOrCreate()
#df_load = sparkSession.read.csv('hdfs://dumbo/user/gx271/pubgETL/mir_death.csv')

with hd.open("hdfs://dumbo/user/gx271/pubgETL/mir_death.csv/part-00006") as f:
    df = pd.read_csv(f)

# convert DataFrame to np array

dat = df.as_matrix()

# dat = np.loadtxt('mydata.csv')

x, y = dat[:,0], dat[:,1]

heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)  
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]  
plt.clf()  
plt.imshow(heatmap, extent=extent)  
# plt.show()
plt.savefig('heatmap.png')
