#Couldn't get mongodb installed on Ubuntu. Various errors from sudo apt-get for core, server packages. Errors occur in the from the installation packages and not my terminal code.
#I have watched through setting up MongoDB on Windows and Ubuntu. I will add some lines that would help to get this task done and explain how I would go about it.

show dbs

use CS3DP19

db.creatUser({
    user:"Milan",
    pwd:"1234",
    roles: ["readWrite", "dbAdmin"]
})

db.createCollection("pages");

show collections

db.pages.insert({
    title: "Wikipedia",
    text: "##Stuff from wikipedia page",
    category: ["Organisation','Website"],
    links: ["##Stuff from the references section on Wikipedia"]
});

db.pages.find();

db.pages.insert([{
    title: "Tilomar Important Bird Area",
    text: "The Tilomar Important Bird Area, also known as Tilomar Forest, is a tract of mainly forested land in East Timor, a country occupying the eastern end of the island of Timor in the Lesser Sunda Islands of Wallacea.",
    category: ["Cova Lima Municipality","Important Bird Areas of East Timor","Natural history of East Timor","Timor Sea","East Timor geography stubs"],
    links: ["http://www.birdlife.org/"]
},{
    title: "Fahrenheit 88",
    text: "Fahrenheit 88 is a shopping centre in Bukit Bintang, Kuala Lumpur, Malaysia. The Fahrenheit 88 building (previously known as KL Plaza) reopened in August 2010 after undergoing extensive renovation works. Management and leasing of the shopping centre is handled by the same company that manages the Pavilion Kuala Lumpur shopping centre.",
    category: ["2010 establishments in Malaysia","Shopping malls in Kuala Lumpur"],
    links: ["https://web.archive.org/web/20110621233327/http://www.dailyexpress.com.my/news.cfm?NewsID=52065","http://www.theedgeproperty.com/news-a-views/1325-kl-plaza-gets-new-name-and-look.html","http://www.malaysiapropertynews.com/2010/01/rm100m-facelift-for-kl-plaza.html","http://www.malaysiapropertynews.com/2010/01/rm100m-facelift-for-kl-plaza.html"]
},{
    title: "Thompson's construction",
    text: "In computer science, Thompson's construction algorithm, also called the McNaughton-Yamada-Thompson algorithm[1], is a method of transforming a regular expression into an equivalent nondeterministic finite automaton (NFA).[2] This NFA can be used to match strings against the regular expression. This algorithm is credited to Ken Thompson. Regular expressions and nondeterministic finite automata are two representations of formal languages. For instance, text processing utilities use regular expressions to describe advanced search patterns, but NFAs are better suited for execution on a computer. Hence, this algorithm is of practical interest, since it can compile regular expressions into NFAs. From a theoretical point of view, this algorithm is a part of the proof that they both accept exactly the same languages, that is, the regular languages. An NFA can be made deterministic by the powerset construction and then be minimized to get an optimal automaton corresponding to the given regular expression. However, an NFA may also be interpreted directly. To decide whether two given regular expressions describe the same language, each can be converted into an equivalent minimal deterministic finite automaton via Thompson's construction, powerset construction, and DFA minimization. If, and only if, the resulting automata agree up to renaming of states, the regular expressions' languages agree.",
    category: ["Finite automata"],
    links: ["https://www.pearson.com/us/higher-education/program/Aho-Compilers-Principles-Techniques-and-Tools-2nd-Edition/PGM167067.html"]
},{
    title: "ω-automaton",
    text: "In automata theory, a branch of theoretical computer science, an ω-automaton (or stream automaton) is a variation of finite automatons that runs on infinite, rather than finite, strings as input. Since ω-automata do not stop, they have a variety of acceptance conditions rather than simply a set of accepting states. ω-automata are useful for specifying behavior of systems that are not expected to terminate, such as hardware, operating systems and control systems. For such systems, one may want to specify a property such as "for every request, an acknowledge eventually follows", or its negation "there is a request that is not followed by an acknowledge". The former is a property of infinite words: one cannot say of a finite sequence that it satisfies this property. Classes of ω-automata include the Büchi automata, Rabin automata, Streett automata, parity automata and Muller automata, each deterministic or non-deterministic. These classes of ω-automata differ only in terms of acceptance condition. They all recognize precisely the regular ω-languages except for the deterministic Büchi automata, which is strictly weaker than all the others. Although all these types of automata recognize the same set of ω-languages, they nonetheless differ in succinctness of representation for a given ω-language.",
    category: ["Finite automata"],
    links: ["https://books.google.com/books?id=wR_oBwAAQBAJ"]
}]);

db.pages.find().pretty();

#Basically update the entry with the title that matches "Wikipedia" (Replaces whole entry)
db.pages.update({title:"Wikipedia"},{
    title:"Wikipedia",
    text:"Wikipedia (/ˌwɪkɪˈpiːdiə/ (About this soundlisten) wik-ih-PEE-dee-ə or /ˌwɪkiˈpiːdiə/ (About this soundlisten) wik-ee-PEE-dee-ə) is a multilingual online encyclopedia created and maintained as an open collaboration project[4] by a community of volunteer editors using a wiki-based editing system.[5] It is the largest and most popular general reference work on the World Wide Web,[6][7][8] and is one of the most popular websites ranked by Alexa as of October 2019.[9] It features exclusively free content and no commercial ads, and is owned and supported by the Wikimedia Foundation, a non-profit organization funded primarily through donations.[10][11][12][13] Wikipedia was launched on January 15, 2001, by Jimmy Wales and Larry Sanger.[14] Sanger coined its name,[15][16] as a portmanteau of "wiki" (the Hawaiian word for "quick"[17]) and "encyclopedia". Initially an English-language encyclopedia, versions of Wikipedia in other languages were quickly developed. With at least 5,992,386 articles,[note 3] the English Wikipedia is the largest of the more than 290 Wikipedia encyclopedias. Overall, Wikipedia comprises more than 40 million articles in 301 different languages[18] and by February 2014 it had reached 18 billion page views and nearly 500 million unique visitors per month.[19] In 2005, Nature published a peer review comparing 42 hard science articles from Encyclopædia Britannica and Wikipedia and found that Wikipedia's level of accuracy approached that of Britannica,[20] although critics suggested that it might not have fared so well in a similar study of a random sampling of all articles or one focused on social science or contentious social issues.[21][22] The following year, Time magazine stated that the open-door policy of allowing anyone to edit had made Wikipedia the biggest and possibly the best encyclopedia in the world, and was a testament to the vision of Jimmy Wales.[23] Wikipedia has been criticized for exhibiting systemic bias, for presenting a mixture of "truth, half truth, and some falsehoods",[24] and for being subject to manipulation and spin in controversial topics.[25] In addition, Wikipedia has gender bias, particularly on its English-language site, where the dominant majority of editors are male. However, Edit-a-thons have been held to encourage female editors and increase the coverage of women's topics.[26][27] Facebook announced that by 2017 it would help readers detect fake news by suggesting links to related Wikipedia articles. YouTube announced a similar plan in 2018.[28]",
    category: ["2001 establishments in the United States","Wikipedia"],
    links: ["https://www.wikipedia.org/", "http://topics.nytimes.com/top/news/business/companies/wikipedia/index.html"]
});

#Set a specific column in entry (Remember extra curly braces)
db.pages.update({title:"Wikipedia"},{$set:{
    text:"Wikipedia (/ˌwɪkɪˈpiːdiə/ (About this soundlisten) wik-ih-PEE-dee-ə or /ˌwɪkiˈpiːdiə/ (About this soundlisten) wik-ee-PEE-dee-ə) is a multilingual online encyclopedia created and maintained as an open collaboration project[4] by a community of volunteer editors using a wiki-based editing system.[5] It is the largest and most popular general reference work on the World Wide Web,[6][7][8] and is one of the most popular websites ranked by Alexa as of October 2019.[9] It features exclusively free content and no commercial ads, and is owned and supported by the Wikimedia Foundation, a non-profit organization funded primarily through donations.[10][11][12][13] Wikipedia was launched on January 15, 2001, by Jimmy Wales and Larry Sanger.[14] Sanger coined its name,[15][16] as a portmanteau of "wiki" (the Hawaiian word for "quick"[17]) and "encyclopedia". Initially an English-language encyclopedia, versions of Wikipedia in other languages were quickly developed. With at least 5,992,386 articles,[note 3] the English Wikipedia is the largest of the more than 290 Wikipedia encyclopedias. Overall, Wikipedia comprises more than 40 million articles in 301 different languages[18] and by February 2014 it had reached 18 billion page views and nearly 500 million unique visitors per month.[19] In 2005, Nature published a peer review comparing 42 hard science articles from Encyclopædia Britannica and Wikipedia and found that Wikipedia's level of accuracy approached that of Britannica,[20] although critics suggested that it might not have fared so well in a similar study of a random sampling of all articles or one focused on social science or contentious social issues.[21][22] The following year, Time magazine stated that the open-door policy of allowing anyone to edit had made Wikipedia the biggest and possibly the best encyclopedia in the world, and was a testament to the vision of Jimmy Wales.[23] Wikipedia has been criticized for exhibiting systemic bias, for presenting a mixture of "truth, half truth, and some falsehoods",[24] and for being subject to manipulation and spin in controversial topics.[25] In addition, Wikipedia has gender bias, particularly on its English-language site, where the dominant majority of editors are male. However, Edit-a-thons have been held to encourage female editors and increase the coverage of women's topics.[26][27] Facebook announced that by 2017 it would help readers detect fake news by suggesting links to related Wikipedia articles. YouTube announced a similar plan in 2018.[28]",
}});

#db.pages.update({title:"Wikipedia"},{$inc:{
    #age:5
#}});

#Remove a Column
#db.pages.update({title:"Wikipedia"},{$unset:{
    #text:1
#}});

#If not found then add as new entry
#db.pages.update({title:"Wikipedia"},{
    #text:1
#},{upsert: true});

#Rename a Column
#db.pages.update({title:"Wikipedia"},{$rename:{"text":"intro"
#}});

#Delete all with title WIkipedia
#db.page.remove({title:"Wikipedia"})

#Delete ONE entry with title WIkipedia
#db.page.remove({title:"Wikipedia"},{justOne: Ture})

db.page.find({title:"Wikipedia"})#Searching as in Task description

db.page.find({$or:[{title:"Wikipedia"},{title:"ω-automaton"}]})

#Doesnt have to be just find by title
#If values then can find via more or less than LTE,GTE,GT,LT (LessThanOrEqualTo,Greater...)

db.page.find().sort({title:1});#Sort by title in ascending order (or -1 for decsending). Can do this after any find() filter
db.page.find().count()#Get number of entries. Can do find first to filter then count the filtered
db.page.find().limit(4)#First 4 entries
db.page.find().pretty()
#can combine all these

#Iterations through entries to print "Webpage Name: {title}"
db.page.find().forEach(function(doc){print("Webpage Name:" +doc.title)});