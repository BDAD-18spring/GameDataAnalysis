val data0 = sc.textFile("matches/agg")

//filter the header
val data1 = data0.filter(!_.split(",")(0).equals("date"))

//date(0),game_size(1),match_id(2),match_mode(3),party_size(4),player_assists(5),player_dbno(6),player_dist_ride(7),player_dist_walk(8),player_dmg(9),player_kills(10),player_name(11),player_survive_time(12),team_id(13),team_placement(14)

val data2 = data1.map(line => Tuple9(line.split(",")(1), line.split(",")(5), line.split(",")(6), line.split(",")(7), line.split(",")(8), line.split(",")(9), line.split(",")(10), line.split(",")(12), line.split(",")(14)))

//player_assist, player_dbno, player_dist_ride, player_dist_walk, player_dmg, player_kills
val data3 = data2.map(tuple => Tuple6(tuple._2.toDouble, tuple._3.toDouble, tuple._4.toDouble, tuple._5.toDouble, tuple._6.toDouble, tuple._7.toDouble))

//[0.0,13.0]
val player_assist = data3.map(_._1).cache
val max1 = player_assist.max
val min1 = player_assist.min

//[0.0, 148.0]
val player_dbno = data3.map(_._2).cache
val max2 = player_dbno.max
val min2 = player_dbno.min

//[0.0, 506175.4]
val player_dist_ride = data3.map(_._3).cache
val max3 = player_dist_ride.max
val min3 = player_dist_ride.min

//[0.0, 1273645.38]
val player_dist_walk = data3.map(_._4).cache
val max4 = player_dist_walk.max
val min4 = player_dist_walk.min

//[0.0, 9408.0]
val player_dmg = data3.map(_._5).cache
val max5 = player_dmg.max
val min5 = player_dmg.min

//[0.0, 94.0]
val player_kills = data3.map(_._6).cache
val max6 = player_kills.max
val min6 = player_kills.min
