spark-shell --driver-memory 4g --executor-memory 4g 

// load dataset
val df = sqlContext.read.json("dota2/dota2.json")

// have an initial understanding of schema of original dataset
df.printSchema()

// keep useful columns
val match_df = df.select(df("match_id"), df("radiant_win"), df("start_time"), df("duration"), df("players.account_id").alias("player_id_list"), df("players.hero_id").alias("hero_id_list"), df("players.item_0").alias("item_0_list"), df("players.item_1").alias("item_1_list"), df("players.item_2").alias("item_2_list"), df("players.item_3").alias("item_3_list"), df("players.item_4").alias("item_4_list"), df("players.item_5").alias("item_5_list"), df("players.kills").alias("kills_list"), df("players.deaths").alias("deaths_list"), df("players.assists").alias("assists_list"))

// remove rows contain Nulls
val matchandplayer_df = match_df.na.drop()

matchandplayer_df.printSchema()

matchandplayer_df.agg(min("start_time"), max("start_time")).head
// [1374071819,1450068932]
// 7-17-2013 to 12-14-2015
matchandplayer_df.agg(min("duration"), max("duration")).head
//[0,16037]

//matchandplayer_df.map(x => x.mkString("|")).saveAsTextFile("dota2/matchandplayer") 


/*
2015-1-1: 1420070400	2015-12-31: 1451606399
2016-1-1: 1451606400	2016-12-31: 1483228799
2017-1-1: 1483228800	2017-12-31: 1514764799
val dota2_df = df.filter($"start_time" > 1420070400 && $"start_time" < 1514764799 )

val tags = List("lobby_type", "human_players", "leagueid", "positive_votes", "negative_votes", "game_mode", "engine", "picks_bans", "parse_status", "chat", "radiant_gold_adv", "radiant_xp_adv", "teamfights", "version", "skill")
for(t <- tags){
   df.drop(t)
}
*/

