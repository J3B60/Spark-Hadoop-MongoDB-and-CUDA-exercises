import sys
from collections import Counter

#Note command line args start with python file so start from arg1 not arg0

for i in sys.argv:
    if i == "map.py":
        continue
    else:
        textfile = i
        file = open(i, "r")
        wordcount = Counter(file.read().split()) #Task takes too much effort, need to find every word, then every stem and lemma. Too much #This is just the basics using a library
        print (textfile + "," + wordcount + "," + ) 
        
#################TODO######################