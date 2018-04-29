val rawData = sc.textFile("pubg")

//remove the header of the CSV
val header = rawData.first()
val data1 = rawData.filter(_ != header)

val data2 = data1.map(line => line.split(','))

val filterData = data2.filter(array => !array(0).equals("")).filter(array => !array(1).equals("")).filter(array => !array(2).equals("")).filter(array => !array(3).equals("")).filter(array => !array(4).equals("")).filter(array => !array(5).equals("")).filter(array => !array(7).equals("")).filter(array => !array(8).equals("")).filter(array => !array(9).equals("")).filter(array => !array(10).equals("")).filter(array => !array(11).equals(""))

//killed_by,killer_name,killer_placement,killer_position_x,killer_position_y,map,time,victim_name,victim_placement,victim_position_x,victim_position_y
val data3 = filterData.map(array => Tuple11(array(0), array(1), array(2).split('.')(0).toInt, array(3).toFloat, array(4).toFloat, array(5), array(7).toInt, array(8), array(9).split('.')(0).toInt, array(10).toFloat, array(11).toFloat))

//killedBy ["AKM", "death.WeapSawnoff_C"]
val killedBy = data3.map(tuple => tuple._1).cache
val min0 = killedBy.min
val max0 = killedBy.max

//killerName ["0----erhu----0", "zzzzzzzzzzzzzzzx"]
val killerName = data3.map(_._2).filter(!_.equals("#unknown")).cache
val min1 = killerName.min
val max1 = killerName.max

//killerPlacement [1, 99]
val killerPlacement = data3.map(_._3).cache
val min3 = killerPlacement.min
val max3 = killerPlacement.max

//killerPositionX [0.0, 814003.2]
val killerPositionX = data3.map(_._4).cache
val min4 = killerPositionX.min
val max4 = killerPositionX.max

//killerPositionY [-10684.67, 814953.9]
val killerPositionY = data3.map(_._5).cache
val min5 = killerPositionY.min
val max5 = killerPositionY.max

//map ["ERANGEL", "MIRAMAR"]
val gameMap = data3.map(_._6).cache
val min6 = gameMap.min
val max6 = gameMap.max

//time [28, 2374]
val gameTime = data3.map(_._7).cache
val min7 = gameTime.min
val max7 = gameTime.max

//victimName ["0----erhu----0", "zzzzzzzzzzzzzzzx"]
val victimName = data3.map(_._8).filter(!_.equals("#unknown")).cache
val min8 = victimName.min
val max8 = victimName.max

// victimPlacement [1, 100]
val victimPlacement = data3.map(_._9).cache
val min9 = victimPlacement.min
val max9 = victimPlacement.max

//victimPositionX [0.0, 814003.2]
val victimPositionX = data3.map(_._10).cache
val min10 = victimPositionX.min
val max10 = victimPositionX.max

//victimPositionY [-10706.09, 814949.8]
val victimPositionY = data3.map(_._11).cache
val min10 = victimPositionY.min
val max10 = victimPositionY.max


