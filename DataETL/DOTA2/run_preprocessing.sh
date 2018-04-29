# Make sure pom.xml is present in the same directory
cd Preprocessing

# Build/compile/Create package using maven
/opt/maven/bin/mvn package

# Execute the process using jar files created in "target" directory
spark-submit --class Preprocessing --master yarn --driver-memory 4g --executor-memory 4g target/scala-0.0.1-SNAPSHOT.jar

# Combine all output data from HDFS into a single file and put on HDFS
hadoop fs -getmerge /user/nl1554/dota2/matchsplayers $HOME/dota2/matchsplayers.txt
hdfs dfs -put dota2/matchsplayers.txt /user/nl1554/dota2/matchsplayers.txt