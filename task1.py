import csv
import numpy as np
import matplotlib.pyplot as plt


def extract(file='Depth Data'):
	fo=open(str(file)+'.csv','r')
	ddata=[]
	l=[]
	flip=-1
	rd=csv.reader(fo)
	for r in rd:
		#print(float(r[1]),end='wawawa\n')
		if flip==1:
			try:
				l=[]
				l.append(float(r[0]))
			except:
				pass
		else:
			try:
				l.append(float(r[1]))
				ddata.append(l)
			except:
				pass
		flip*=-1
	#print(ddata)
	fo.close()
	return ddata
def plotd(data=extract(),n=5,m=2):
	print(data)
	x=[]
	y=[]
	plt.ion()
	fig,ax=plt.subplots()
	ax.set_xlabel("Time (s)")
	ax.set_ylabel("Depth(m)")
	line, = ax.plot([], [])
	for i in data:
		x.append(i[0])
		y.append(i[1])
		#print(i,end='ehehe\n')
		'''will it be a good idea to use 
		the standard deviation of already plotted data
		 to handle erratic data?
		like if the next depth is more than n (real no.) sd's 
		away from the mean of depths in the last m(maybe 5 or 10) seconds
		then don't plot it? maybe. maybe not. idk lol'''
		#n=0
		#m=0
		sd=np.std(y[len(y)-(1+n):len(y)-1])
		mean=np.mean(y[len(y)-(1+n):len(y)-1])
		if abs(mean-y[-1])>m*abs(sd):
			pass
		else:
			line.set_data(x,y)
			ax.relim()
			ax.autoscale_view()
			fig.canvas.draw_idle()
			plt.pause(0.1)
		#print(y,end='\n')
	plt.pause(1000)

data=extract()
plotd(data,5,1)		
		
