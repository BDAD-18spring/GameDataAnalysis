# GameDataAnalysis

Game data analysis for PUBG and DOTA2

![UI Rendering](https://github.com/BDAD-18spring/GameDataAnalysis/blob/master/WebApplicationScreenshots/1_index.png)

## Data Source

- PUBG matches and death data pulled from [TRN PUBG Tracker API](https://pubgtracker.com/site-api)
- DoTA2 matches data obtained from YASP's data dumps that located on [Academic Torrents](http://academictorrents.com)

## Environment

- NYU HPC Dumbo
- NYU CIMS Web Server linserv2
- Apache Spark 1.6.0
- python 2.7.11 with packages `numpy`, `matplotlib`, `pyspark`, `pydoop`
- pandas 0.18.1
- flask & wtforms

## Data ETL

For **PUBG death data**, run `pubgDeathDataETL.scala` and store the output files on HDFS under `pubgETL/pubg_death.csv` folder. 

For **PUBG heat map data**, Run `HeatMap.scala` and store the output files on HDFS under `pubgETL/mir_death.csv` and `pubgETL/era_death.csv` folders. 

For **Random Forest Regression LIBSVM** data, run `GenerateLIBSVM.scala` and save files under HDFS's `matches/libsvm/libsvm_data.txt` folder.

For **DoTA2** data, following commands in `run_preprocessing.sh` and save files under HDFS's `dota2/matchsplayers.txt` folder.

## PUBG Death Heat Map

Use `heatmap.py` to generate the heat map of PUBG death zones on both **MIRAMAR** and **ERANGEL** maps

## PUBG Player Analysis With Random Forest Regression Model

Use `TeamPlacementPrediction.scala` to generate the predictive model of team placement and skill scores of players in PUBG matches.

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

## DoTA2 Match Result Prediction Wtih Random Forest Classification Model

Use `MatchResultPrediction.py` to generate the predictive model of match result in DoTA2 matches.

The features' IDs and their names are listed below:

| Feature_ID | Feature_name        |
| ---------- | ------------------- |
| 1          | rediant_heros       |
| 2          | rediant_items       |
| 3          | dire_heros          |
| 4          | dire_items          |

## Web Application
Follow commands in `WebApplication/run.sh` to start the web app server for interactive use of our project's application.


## Author
* [Gen Xiang](gx271@nyu.edu)(gx271@nyu.edu) 
* [Nan Liu](nl1554@nyu.edu)(nl1554@nyu.edu)
