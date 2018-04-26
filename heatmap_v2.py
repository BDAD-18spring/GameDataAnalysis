# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
%matplotlib inline

from scipy.misc.pilutil import imread

# import only a few datasets for now
deaths1 = pd.read_csv("~/BDAD/PUBGdata/deaths/kill_match_stats_final_0.csv")
deaths2 = pd.read_csv("~/BDAD/PUBGdata/deaths/kill_match_stats_final_1.csv")
deaths3 = pd.read_csv("~/BDAD/PUBGdata/deaths/kill_match_stats_final_2.csv")
deaths4 = pd.read_csv("~/BDAD/PUBGdata/deaths/kill_match_stats_final_3.csv")
deaths5 = pd.read_csv("~/BDAD/PUBGdata/deaths/kill_match_stats_final_4.csv")

deaths = pd.concat([deaths1, deaths2, death3, death4, death5])

deaths.head

# restrict to miramar
miramar = deaths[deaths["map"] == "MIRAMAR"]
erangel = deaths[deaths["map"] == "ERANGEL"]

# scale positions to size of miramar.jpg = 1000x1000 and erangel.jpg = 4096x4096
position_data = ["killer_position_x","killer_position_y","victim_position_x","victim_position_y"]
for position in position_data:
    miramar[position] = miramar[position].apply(lambda x: x*1000/800000)
    miramar = miramar[miramar[position] != 0]
    
    erangel[position] = erangel[position].apply(lambda x: x*4096/800000)
    erangel = erangel[erangel[position] != 0]

# select random sample of early deaths = deaths in the first 2 minutes 
# restrict to n, so that kdeplot doesn't take too long
n = 10000
mira_sample = miramar[miramar["time"] < 100].sample(n)
eran_sample = erangel[erangel["time"] < 100].sample(n)

# heatmap of mira
bg = imread("./pic/input/miramar.jpg")
fig, ax = plt.subplots(1,1,figsize=(15,15))
ax.imshow(bg)
sns.kdeplot(mira_sample["victim_position_x"], mira_sample["victim_position_y"], n_levels=100)

# heatmap of eran
bg = imread("./pic/erangel.jpg")
fig, ax = plt.subplots(1,1,figsize=(15,15))
ax.imshow(bg)
sns.kdeplot(eran_sample["victim_position_x"], eran_sample["victim_position_y"], n_levels=100)
