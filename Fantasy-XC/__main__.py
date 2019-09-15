#Imports: leave these alone
from Race import Race
from Player import Player
from League import League

#Players in the fantasy XC league
players=[]

players+=[Player("Aaron",[
	"Jovi Tseng",
	"Aaron Diamond",
	"Dexter Griffin",
	"Theo Schmitt",
	"Jalen Madjidi",
	"Katherine Cherney",
	"Alana Lee"])
	]

players+=[Player("Beck",[
	"Hanna",
	"Kieran Sullivan",
	"Lianna Leung",
	"Luke de Valpine",
	"Charlie Werner",
	"Emma Shamir",
	"Rudy Cipollone"])
	]

players+=[Player("Will",[
	"Taylor Yee",
	"Joe",
	"Aiko",
	"Emmett Gardella",
	"Leah",
	"Natalie",
	"Roman Jackson"])
	]

players+=[Player("Quinn",[
	"Lily Kung",
	"Ari",
	"Ela",
	"Aidan Metcalfe",
	"Anne",
	"Julian Currier",
	"Emma"])
	]

players+=[Player("Aiden",[
	"Tali",
	"Elliot",
	"Julien Chauvet",
	"Tia Bottger",
	"Colleen",
	"Cory Irie",
	"Theodore"])
	]

players+=[Player("Milo",[
	"Quinn Koch",
	"William Fernholz",
	"Susana",
	"Milo Moses",
	"Beck Tompkins",
	"Kai Kumar",
	"Nick"])
	]


#Files for the data
files=[]
files+=[["Ed_Sias_Frosh-Soph_Boys",False]]
files+=[["Ed_Sias_Frosh-Soph_Girls",False]]
files+=[["Ed_Sias_Varsity_Girls",True]]
files+=[["Ed_Sias_Varsity_Boys",True]]
files+=[["Ed_Sias_Frosh_Boys",False]]


#Declaring league
L=League(players)

#Adding races to league
for file in files:
	race=Race(file[0],file[1])
	L.scoreAdd(race)

#Printing points
print(L)

#Graphing
L.graph(["Ed_Sias_Frosh-Soph_Boys","Ed_Sias_Varsity_Boys","Ed_Sias_Frosh_Boys"])

