######TASK 2 #########
d = dataflow.read("file.csv")
# Analyse what this could compute based on the definiton of the operators below

flat = d.map(lambda t: (t[0], eval(t[3])))
bd = flat.filter(lambda t: t[1] == "CS3DP")
bd.write("out.csv")

# Analyse what this could compute based on the definiton of the operators
z = flat.group(lambda t: t[1])
r = z.reduce(lambda tl: len(tl))
print(r)
#######################

########TASK 3##########
#No CSV file provided, no scenraio provided to work with.
#I understand how this is all meant to work and how the functions work.
#I wish I was given a task to work on rather than coming up with something on my own or 
#searching the internet for example task.
#I understand how this all works, I learnt a lot by just making the pipe diagram in Task 2 and 
#understand how this works. I will just take note of the functions here and how they work for 
#future reference if I ever need it.

#######FUNCS##############

#reads in the CSV file contents as list of tuples
read(file)
#EXAMPLE var = read(FilePATH) #Read file into the variable. Self explanitory

#writes output to file
write(file)
#EXAMPLE var.write(filePATH) #writes the variable or what ever to the filepath

#filter list of tuples for which function(t) returns True
filter(function(t))
#EXAMPLE filter(lambda t[0]: t[0] == 'Something')) #Filter stuff, again just like Pandas or SQL, self explanitory

#transforms input (the list of tuples) into proper key,value tuple pairs for mapReduce
map(function(t))
#EXAMPLE map(lambda t: (t[0], eval(t[3]))#From Task 2 just as pipe diagram in mapReduce folder says, it takes only these two columns from the input CSV file and uses it as key,value pair tuples

#Group just like SQL or Pandas style
group(function(t))
#EXAMPLE group(lambda x : x[0])

#applies reduction function to all data (or each group if group() applied obviously). Returns single tuple (or one for each group) [the best example is to imagine a count function to count number of entries in each group].
reduce(function(t))
#EXAMPLE reduce(lambda t: len(t)) #Basically Count

#join any tuple from x with any tuple from y by calling the func function(tx,ty) on each pair of tuples
join(y,function(tx,ty))

########END OF FUNCS#######
#all function(t)'s are usually lambda functions which are single line and none refereable but keep the code clean and 
#easy to read. These functions aren't overly complicated either.

#Note simple lambda functions like (lambda x: x[0]) means for every entry in the list, take the first item of the tuple.
#Remeber we work with a list of tuples so [(x,2),(y,2),(z,3)] so there are two levels of [#] reference.