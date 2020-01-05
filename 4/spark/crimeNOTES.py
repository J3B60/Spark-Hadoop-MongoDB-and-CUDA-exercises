CSVRDD = (sc.textFile("filepath").map(lambda element: element.split("\t")))#Optional #, minPartitions= #Number
CSVRDD.take(#Number)
CSVRDD.getNumPartitions()
CSVRDD.count()#NUmber of rows/entries
CSVRDD.map(#Pass a function here)
CSV.flatMap(#Pass a function here)#Makes it horizontal rather than vertical list
CSVRDD.filter(#Filter Function eg lambda func)
CSVRDD.distinct().take()#Unique values
CSVRDD.groupByKey()
CSVRDD.mapValues(sum).map()# Count of each unique word
CSVRDD.groupBy(#Filter Lambda)#Eg filter by first 3 letters matching
CSVRDD.sample()#Take sample (args: False, 0.1) 0.1= percentage of data, False=with replacment(probability replacment)
CSVRDD.join()#Join RDDs# Differnt joins exist eg, left, right, outer, inner etc
CSVRDD.reduce(#Function/Method/Lambda)#Remove elements
CSVRDD.reduceByKey(#Function/Lambda/Method)#By key basis (collect keys togeter as in mapReduce Hadoop)
CSVRDD.union()#union
CSVRDD.intersection()#Intersect (common values)
CSVRDD.collect()#For smaller RDD (Similar to .take() except it takes all) (collect takes a long time)
CSVRDD.saveAsTextFile("filepath")
CSVRDD.sortByKey(True, 1) #default Ascending(Pass True or for descending False) (also pass 1)
CSVRDD.mapPartitionWithIndex(#Function)
CSVRDD.subtract()#Subract one RDD from another
CSVRDD.cartesian()#Cartesian product of two RDD(mapping one RDD to another)

#I have attempted the task and have been unsuccessful at grouping the columns of crimedesc. I think I should 'clean' the data a bit better. I have been getting the seperate entries of data but I think I should have just 'cleaned' it to have the crimedesc columns alone and then loading it into an RDD. this way I can do map and reduce to get the count I need of crimedescs. I wish it was clearer with what is meant by 'cleaning' because it took a while to figure out :( It would at least be nice to have an example python file to run since it also took a while and I was unable to load pyspark into py so I had to write everything directly into the pyspark console rather than having a py file.