import org.apache.spark.mllib.tree.RandomForest
import org.apache.spark.mllib.tree.model.RandomForestModel
import org.apache.spark.mllib.util.MLUtils

// Load and parse the data file.
val data = MLUtils.loadLibSVMFile(sc, "matches/libsvm/libsvm_data.txt")
// Split the data into training and test sets (30% held out for testing)
val splits = data.randomSplit(Array(0.7, 0.3))
val (trainingData, testData) = (splits(0), splits(1))

// Train a RandomForest model.
// Empty categoricalFeaturesInfo indicates all features are continuous.
val numClasses = 2
val categoricalFeaturesInfo = Map[Int, Int]()
val numTrees = 10 // Use more in practice.
val featureSubsetStrategy = "auto" // Let the algorithm choose.
val impurity = "variance"
val maxDepth = 4
val maxBins = 32

val model = RandomForest.trainRegressor(trainingData, categoricalFeaturesInfo,
  numTrees, featureSubsetStrategy, impurity, maxDepth, maxBins)

// Evaluate model on test instances and compute test error
val labelAndPreds = testData.map { point =>
  val prediction = model.predict(point.features)
  (point.label, prediction)
}

//val testErr = labelAndPreds.filter(r => r._1 != r._2).count.toDouble / testData.count()
//println(s"Test Error = $testErr")

val testMSE = labelAndPreds.map{ case(v, p) => math.pow((v - p), 2)}.mean()
println("Test Mean Squared Error = " + testMSE)
println(s"Learned classification forest model:\n ${model.toDebugString}")

val vector = model.featureImportances()
println(" ")
println("-----------Feature Importnaces------------")
println("player_assists: " + vector(0))
println("player_dbno: " + vector(1))
println("player_dist_ride: " + vector(2))
println("player_dist_walk: " + vector(3))
println("player_dmg: " + vector(4))
println("player_kills: " + vector(5))
println("player_survive_time: " + vector(6))

// Save and load model
model.save(sc, "RandomForestModel/myRandomForestRegressionModel")

// val sameModel = RandomForestModel.load(sc, "target/tmp/myRandomForestClassificationModel")

