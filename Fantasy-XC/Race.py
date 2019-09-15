import matplotlib.pyplot as plt
import os
class Race():

	def __init__(self,filepath,var):
		self.name=filepath
		dir_path = os.path.dirname(os.path.realpath(__file__))
		filepath=f"{dir_path}"+"/Races/"+filepath+".txt"
		with open(filepath,"r",errors='replace') as g:
			f=g.readlines()
			f=[f[i] for i in range(len(f)) if i%2==0]
			f=[i.split("\t") for i in f]
			f=[[i[2]]+[i[4]] for i in f]
			d={}
			for i in range(len(f)):
				d[f[i][0]]=f[i][1]

		self.data=d
		self.var=var
		self.size=len(d.keys())

	def contains(self,name):

		return name in self.data.keys()

	def time(self,name):
		if not self.contains(name):
			return -1

		else:
			return self.data[name]

	def place(self,name):
		count=0
		if not self.contains(name):
			return 0

		for key in self.data.keys():
			if self.data[key]<self.data[name]:
				count+=1

		return count

	def points(self,name):
		if not self.contains(name):
			return 0

		if self.var:
			return 1.5*(self.size-self.place(name))/self.size

		return (self.size-self.place(name))/self.size

	def graph(self):
		data=[self.data[key] for key in self.data.keys()]
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
			points+=[[data[i],temp]]
		plt.scatter([p[0] for p in points], [p[1] for p in points], alpha=0.5)
		plt.xlabel('time (min)')
		plt.ylabel('density of people')
		plt.show()

