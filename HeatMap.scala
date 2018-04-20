val data0 = sc.textFile("pubgETL/pubg_death.csv")
val victimPos = data0.map(line => Tuple3(line.split(',')(5), line.split(',')(9), line.split(',')(10)))

val MIRmap = victimPos.filter(_._1.equals("MIRAMAR"))
val ERAmap = victimPos.filter(_._1.equals("ERANGEL"))

val mir = MIRmap.map(tuple => tuple._2 + "," + tuple._3)
val era = ERAmap.map(tuple => tuple._2 + "," + tuple._3)

mir.saveAsTextFile("pubgETL/mir_death.csv")
era.saveAsTextFile("pubgETL/era_death.csv")
