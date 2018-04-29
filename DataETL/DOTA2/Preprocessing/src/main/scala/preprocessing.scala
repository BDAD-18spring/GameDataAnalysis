import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf


object Preprocessing {
  def main(args: Array[String]) {
    val sc = new SparkContext(new SparkConf().setAppName("Dota2 Data Preprocessing"))
    
    // load original json file from hdfs
    val sqlContext = new org.apache.spark.sql.SQLContext(sc)
    val df = sqlContext.read.json("dota2/dota2.json")

    // discard useless columns
    val match_df = df.select(df("match_id"), df("radiant_win"), df("start_time"), df("duration"), df("players.account_id").alias("player_id_list"), df("players.hero_id").alias("hero_id_list"), df("players.item_0").alias("item_0_list"), df("players.item_1").alias("item_1_list"), df("players.item_2").alias("item_2_list"), df("players.item_3").alias("item_3_list"), df("players.item_4").alias("item_4_list"), df("players.item_5").alias("item_5_list"), df("players.kills").alias("kills_list"), df("players.deaths").alias("deaths_list"), df("players.assists").alias("assists_list"))
    val matchandplayer_df = match_df.na.drop()

    // output processed data
    matchandplayer_df.map(x => x.mkString("|")).saveAsTextFile("dota2/matchsplayers") 
    //test.write.format("com.databricks.spark.csv").option("header", "true").save("dota2/dota2.csv")
  }
}
