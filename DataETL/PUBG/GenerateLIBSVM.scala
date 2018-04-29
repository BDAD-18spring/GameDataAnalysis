val data0 = sc.textFile("matches")

//filter the header
val data1 = data0.filter(!_.split(",")(0).equals("date"))

//date(0),game_size(1),match_id(2),match_mode(3),party_size(4),player_assists(5),player_dbno(6),player_dist_ride(7),player_dist_walk(8),player_dmg(9),player_kills(10),player_name(11),player_survive_time(12),team_id(13),team_placement(14)

// party_size * game_size = maximum number of players in this game
// team_placement_rate = team_placement / game_size
val data2 = data1.map(line => Tuple9(line.split(",")(1), line.split(",")(5), line.split(",")(6), line.split(",")(7), line.split(",")(8), line.split(",")(9), line.split(",")(10), line.split(",")(12), line.split(",")(14)))

//Songnan Zhang: spicechicken9527
val data3 = data2.map(tuple => Tuple8(tuple._9.toDouble/tuple._1.toDouble, tuple._2, tuple._3, tuple._4, tuple._5, tuple._6, tuple._7, tuple._8))

val data4 = data3.map(tuple => tuple._1 + " 1:" + tuple._2 + " 2:" + tuple._3 + " 3:" + tuple._4 + " 4:" + tuple._5 + " 5:" + tuple._6 + " 6:" + tuple._7 + " 7:" + tuple._8)

data4.saveAsTextFile("matches/libsvm/libsvm_data.txt")
