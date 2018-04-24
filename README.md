# GameDataAnalysis

Game data analysis for PUBG and DOTA2

![UI Rendering](https://github.com/BDAD-18spring/GameDataAnalysis/blob/master/UI%20Rendering.jpg)

## Data Source

- PUBG matches and death data pulled from [TRN PUBG Tracker API](https://pubgtracker.com/site-api)
- DoTA2 matches data from ...

## Environment

- NYU HPC Dumbo
- python 2.7.11 with packages `numpy`, `matplotlib`, `pyspark`, `pydoop`
- Apache Spark 1.6.0
- pandas 0.18.1

## Data ETL

For **PUBG death data**, run `pubgDeathDataETL.scala` and store the output files on HDFS under `pubgETL/pubg_death.csv` folder. 

For **PUBG heat map data**, Run `HeatMap.scala` and store the output files on HDFS under `pubgETL/mir_death.csv` and `pubgETL/era_death.csv` folders. 

For **Random Forest Regression LIBSVM** data, run `GenerateLIBSVM.scala` and save files under HDFS's `matches/libsvm/libsvm_data.txt` folder.

## Heat Map

Use `heatmap.py` to generate the heat map of PUBG death zones on both **MIRAMAR** and **ERANGEL** maps

## Random Forest Regression Model

Use `TeamPlacementPrediction.scala` to generate the predictive model of team placement in PUBG matches.

The features' IDs and their names in LIBSVM output are listed below:

| Feature_ID | Feature_name        |
| ---------- | ------------------- |
| 1          | player_assists      |
| 2          | player_dbno         |
| 3          | player_dist_ride    |
| 4          | player_dist_walk    |
| 5          | player_dmg          |
| 6          | player_kills        |
| 7          | player_survive_time |

