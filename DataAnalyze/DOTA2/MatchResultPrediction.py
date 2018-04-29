################################################################
# 
# Start pyspark with following command:
# pyspark --driver-memory 4G
# 
################################################################

import pandas as pd
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.tree import LabeledPoint

def convert2Vector(line):
	# match_id = [int(line[0])]
	radiant_win = [1 if line[1]=='true' or line[1]=='True' else 0]
	rediant_heroes = [0] * heroes_count
	dire_heroes = [0] * heroes_count
	rediant_items = [0] * items_count
	dire_items = [0] * items_count
	match_heroes = line[5].split(",")
	for rh in match_heroes[:5]:
		if rh.strip() in heroes_index.keys():
			idx = heroes_index[rh.strip()]
			rediant_heroes[idx] = 1
	for dh in match_heroes[5:]:
		if dh.strip() in heroes_index.keys():
			idx = heroes_index[dh.strip()]
			dire_heroes[idx] = 1
	for i in range(6,12):
		match_items = line[i].split(",")
		for ri in match_items[:5]:
			if ri.strip() in items_index.keys():
				idx = items_index[ri.strip()]
				rediant_items[idx] = 1
		for di in match_items[5:]:
			if di.strip() in items_index.keys():
				idx = items_index[di.strip()]
				dire_items[idx] = 1
	# ['rediant_win', 'rediant_hero1', 'rediant_hero2', ..., 'rediant_item1', 'rediant_item2', ..., 'dire_hero1', 'dire_hero2', ..., 'dire_item1', 'dire_item2',.., ]
	return radiant_win + rediant_heroes + rediant_items + dire_heroes + dire_items
	# return rediant_heroes + rediant_items + dire_heroes + dire_items, radiant_win


def convert2libsvm(line):
	libsvm = []
	libsvm.append(str(line[0]))
	for i, item in enumerate(line[1:]):
		new_item = "%s:%s" % (i + 1, item)
		libsvm.append(new_item)
		new_line = " ".join(libsvm)
		new_line += "\n"
	return new_line


def convert2labeledpoint(line):
	line = [float(x) for x in line]
	return LabeledPoint(line[0], line[1:])


# schema of match dataset
# 0 match_id Int
# 1radiant_win Bool
# 2 start_time Int
# 3 duration int
# 4 player_id_list array[int]
# 5 hero_id_list array[int]
# 6 item_0_list array[int]
# 7 item_1_list array[int]
# 8 item_2_list array[int]
# 9 item_3_list array[int]
# 10 item_4_list array[int]
# 11 item_5_list array[int]
# 12 kills_list array[int]
# 13 deaths_list array[int]
# 14 assists_list array[int] 
matches = sc.textFile('dota2/matchsplayers.txt').map(lambda line: line.replace('WrappedArray(', '').replace(')', '').split("|"))

# get list of heroes
heroes_names = sc.textFile('dota2/hero_names.csv')
heroes_header = heroes_names.first()
heroes = heroes_names.filter(lambda line: line != heroes_header).map(lambda line: line.split(",")[1])
heroes_count = heroes.count()
# 112
heroes_index = heroes.zipWithIndex().collectAsMap()

# get list of items
items_names = sc.textFile('dota2/item_ids.csv')
items_header = items_names.first()
items = items_names.filter(lambda line: line != items_header).map(lambda line: line.split(",")[0])
items_count = items.count()
# 189
items_index = items.zipWithIndex().collectAsMap()

# radiant_heroes = heroes.map(lambda hero: 'radiant_' + hero)
# radiant_items = heroes.map(lambda item: 'radiant_' + item)
# dire_heroes = heroes.map(lambda hero: 'dire_' + hero)
# dire_items = heroes.map(lambda item: 'dire_' + item)
# init_heroes = [0] * heroes_count
# init_items = [0] * items_count

radiant_dire = matches.map(lambda line: convert2Vector(line))
# X = matches.map(lambda line: convert2Vector(line)[0])
# Y = matches.map(lambda line: convert2Vector(line)[1])
data = radiant_dire.map(lambda line: convert2labeledpoint(line))

# Split the data into training and test sets (30% held out for testing)
trainingData, testData = data.randomSplit(weights=[0.7, 0.3], seed=1)

# Train model with RandomForestClassifier
model = RandomForest.trainClassifier(trainingData, numClasses=2, categoricalFeaturesInfo={}, numTrees=3, featureSubsetStrategy="auto", impurity='gini', maxDepth=4, maxBins=32)

# Evaluate model on test instances and compute test error
predictions = model.predict(testData.map(lambda x: x.features))
labels_and_predictions = testData.map(lambda x: x.label).zip(predictions)
acc = labels_and_predictions.filter(lambda x: x[0] == x[1]).count() / float(testData.count())
print("Accuracy of Model: %.3f%%" % (acc * 100))
# Accuracy of Model: 74.227%

# Save and load model
model.save(sc, "Dota2RandomForestModel")

# Test loading model
# test_model = RandomForestModel.load(sc, "Dota2RandomForestModel")
# line = data.first().features
# model.predict(line)