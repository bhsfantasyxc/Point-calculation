import pylab 
from Race import Race
class League:

	def __init__(self,players,races=[]):
		self.races=races
		self.players=players

	def __str__(self):
		out="Players: \n"
		for i in self.players:
			out+="\t"+str(i.name)+" ("+str(int(i.points*100)/100)+") "+": \n"
			for j in range(len(i.runners)):
				out+="\t \t "+i.runners[j]+" ("+str(int(i.runnerPoints[j]*100)/100)+") "+"\n"

		out+="Races: \n"
		for i in self.races:
			if i.var:
				out+="\t"+i.name+" (var) "+"\n"
			else:
				out+="\t"+i.name+" (jv) "+"\n"
		return out
	
	def scoreAdd(self,race):

		self.races+=[race]
		for player in self.players:
			player.getPoints(race)

	def graph(self,myRaces=-1):
		if myRaces==-1:
			myRaces=[race.name for race in self.races]

		myRaces=[Race(race,True) for race in myRaces]
		
		for S in myRaces:
			data=[S.data[key] for key in S.data.keys()]
			for i in range(len(data)):
				num=data[i]
				num=num.split(":")
				num=float(num[0])+float(num[1])/60
				data[i]=num

			data=sorted(data)

			points=[]


			for i in range(len(data)):
				temp=0
				temp+=sum([1 for d in data if abs(d-data[i])<.7])
				points+=[[data[i],temp/S.size]]
			pylab.plot([p[0] for p in points], [p[1] for p in points],linewidth=3.0,label=S.name)
		
		pylab.xlabel('time (min)')
		pylab.ylabel('density of people')
		pylab.legend(loc='upper right')
		pylab.show()
		