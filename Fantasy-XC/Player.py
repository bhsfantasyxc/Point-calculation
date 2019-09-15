class Player:

	def __init__(self,name,runners):
		self.name=name
		self.runners=runners
		self.points=0
		self.runnerPoints=[0 for i in range(len(runners))]

	def getPoints(self,race):

		for i in range(len(self.runners)):
			self.runnerPoints[i] += race.points(self.runners[i])
		self.points=sum(self.runnerPoints)