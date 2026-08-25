#NAME: Thejas Shetty
#ID: 2026B5PS1257H


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
	'''sds=[]
	mans=[]'''
	plt.ion()
	fig,ax=plt.subplots()
	ax.set_xlabel("Time (s)")
	ax.set_ylabel("Depth(m)")
	line, = ax.plot([], [])
	rejected=0
	for i in data:
		if data.index(i)==0:
			x.append(i[0])
			y.append(i[1])
		#print(i,end='ehehe\n')
		'''will it be a good idea to use 
		the standard deviation of already plotted data
		 to handle erratic data?
		like if the next depth is more than n (real no.) sd's 
		away from the mean of depths in the last m(maybe 5 or 10) seconds/steps
		then don't plot it? maybe. maybe not. idk lol'''
		#n=0
		#m=0
		sd=np.std(y[len(y)-(1+n):len(y)])
		mean=np.mean(y[len(y)-(1+n):len(y)])
		'''#test:
		sds.append(sd)
		mans.append(mean)
		#test end(?)'''
		if abs(mean-i[1])>max(m*abs(sd),5) and len(y)>=5: #alternate idea:use mean of sd's to do this thing 
			#print(mean-y[-1],sd,'\n')
			rejected+=1#consecutively rejected entries
		else:
			x.append(i[0])
			y.append(i[1])
			line.set_data(x,y)
			ax.relim()
			ax.autoscale_view()
			fig.canvas.draw_idle()
			plt.pause(1)
			rejected=-1   #now it doesn't represent consecutively rejected but it's to let the data append ,rejected. times to update sd to prevent freezing too much
		#print(y,end='\n')
		#print(sds,mans,sep='hi',end='bye\n')
	plt.pause(1000)
	
data=extract()
plotd(data,5,8)
#reasonably keep m in range of 5 to 10(when n=5). 3 will give you a curve with less janky points but the jankiness at that scale might actually be true 		
		
