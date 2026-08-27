#NAME: Thejas Shetty
#ID: 2026B5PS1257H
'''now I'll try to make it smoother
at first i thought of dealing with means again
but now i think it's better to think in terms of slope. 
what would the mean(or weighted mean in some ratio) of the recorded data and the idealized point based on median of slopes..
but better do that after collecting some data. idk if this will work. current time: 23:03 27th aug'''
#NOT WORKING YET! wildly incorrect and incomplete graph, so this was jusr a try.
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
	#print(data)
	x=[]
	y=[]
	slopes=[]
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
			try:
				
				if len(y)>5:
					slope=(y[-1]-y[-2])/(x[-1]-x[-2])
					slopes.append(slope)
					if len(slopes)>n+1:
						smean=mean=np.mean(y[len(slopes)-(1+n):len(slopes)])
					elif len(slopes)>1:
						smean=np.mean(slopes)
					else:
						smean=slope
					y_ideal=smean*(x[-1]-x[-2])+y[-2]
					y_measured=y.pop()
					y.append((y_measured+y_ideal)/2)
					#slopes.pop()
					#slope=(y[-1]-y[-2])/(x[-1]-x[-2])
					slopes.append(slope)
			except:
				if len(x)>len(y):
					y.append(i[1])
			line.set_data(x,y)
			ax.relim()
			ax.autoscale_view()
			fig.canvas.draw_idle()
			plt.pause(0.1)
			rejected=-1   #now it doesn't represent consecutively rejected but it's to let the data append ,rejected. times to update sd to prevent freezing too much
		#print(y,end='\n')
		#print(sds,mans,sep='hi',end='bye\n')
	plt.pause(1000)
	
data=extract()
plotd(data,5,4)
#reasonably keep m in range of 5 to 10(when n=5). 3 will give you a curve with less janky points but the jankiness at that scale might actually be true 		

