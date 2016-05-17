import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
import numpy as np
import seaborn as sns
import pandas as pd
import math
import csv

sns.set(style="darkgrid", color_codes=True) #make it look nice

"""
for this part of the project data has to be manipulated in many ways
"""
#this is the years in the format written in the csv
years = ["2011-12", "2012-13","2013-14","2014-15","2015-16"]
#districts use the rest are special districts 
districts = [dist for dist in range(1,33)]
x = [i for i in range(0,32)]

data = {}
#create list for each year 
for year in years:
    data["TotalEnroll" + year] = []
    data["EngLearn" + year] = []
    data["nEngLearn" + year] = []
    data["Poverty" + year] = []
    data["nPoverty" + year] = []
    data["EngLearn#" + year] = []
    data["nEngLearn#" + year] = []
    data["Poverty#" + year] = []
    data["nPoverty#" + year] = []
#list for means for all districts
meanTot = []
meanEng = []
meanNEng = []
meanPov = []
meanNPov = []
#list for each district
#for dist in districts:
#    data['Total

#get some data (this is not divided by district)
with open('school/district.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        for year in years:
            #this way they are appended sorted by district
            if(row['Year'] == year and int(row['District']) < 33):
                data["TotalEnroll" + year].append(float(row['Total Enrollment']))
                data["EngLearn" + year].append(float(row[' English Language Learners']))
                data["nEngLearn" + year].append(100- float(row[' English Language Learners']))
                data["Poverty" + year].append(float(row[' Poverty']))
                data["nPoverty" + year].append(100- float(row[' Poverty']))
                data["EngLearn#" + year].append(int(row['# English Language Learners']))
                data["nEngLearn#" + year].append(int(row['Total Enrollment']) - int(row['# English Language Learners']))
                data["Poverty#" + year].append(int(row['# Poverty']))
                data["nPoverty#" + year].append(int(row['Total Enrollment']) - int(row['# Poverty']))
            
#got this part of the code from - http://stackoverflow.com/questions/20792445/calculate-rgb-value-for-a-range-of-values-to-create-heat-map
def floatRgb(mag, cmin, cmax,color):
    try:
        # normalize to [0,1]
        x = float(mag-cmin)/float(cmax-cmin)
    except:
        # cmax = cmin
        x = 0.5
    if(color==0):
        blue=min((max((4*(0.75-x), 0.)), 1.))
        red=0
        green=0
    elif(color==1):
        blue=0
        red=min((max((4*(0.75-x), 0.)), 1.))
        green=0
    elif(color==2):
        blue=0
        red=0
        green=min((max((4*(0.75-x), 0.)), 1.))
    elif(color==3):
        blue=min((max((4*(0.55-x), 0.)), 1.))
        red=0.50
        green=0.10
    elif(color==4):
        blue=0.5
        red=min((max((4*(0.55-x), 0.)), 1.))
        green=0.1
    else:
        blue=min((max((4*(0.75-x), 0.)), 1.))
        red=min((max((4*(x-0.50), 0.)), 1.))
        green=min((max((4*math.fabs(x-0.5)-1., 0.)), 1.))
    return (red, green, blue)

#quick function to plot maps in same grap
def plotMap(list,plot,color,title,fig):
    #nyc locations
    lllat = 40.4712
    lllon = -74.3018
    urlat = 40.9331
    urlot = -73.7026
 #   fig0, ax0 = plt.subplots(plot)
    ax      = fig.add_subplot(plot)
    ax.set_title(title)
    map = Basemap(llcrnrlon=lllon,llcrnrlat=lllat,urcrnrlon=urlot,urcrnrlat=urlat,
                  resolution='c')
    map.readshapefile('2013-2014 School Zones/geo_export_39005c22-779d-4640-a869-9910e115f69a', 'shape')
    for info, shape in zip(map.shape_info, map.shape):
        for d in districts:
            if info['schooldist'] == d:
                c = floatRgb(list[d-1],min(list),max(list),color)
                s = []
                s.append(Polygon(np.array(shape), True))
                dist = ax.add_collection(PatchCollection( s, facecolor= c, edgecolor='k', linewidths=1., zorder=2))
 #               ax.colorbar(map)
def mapPlots():
#mapping 5 graphs for each year 
    figNum = 1
    for year in years:
        fig = plt.figure(figNum)
        name = year+ " NYC School District Change Poverty and English Learners"
        plt.suptitle(year+ " NYC School District Change Poverty and English Learners")
        plotMap(data["TotalEnroll"+year],231,0,"Total Enroll "+year,fig)
        plotMap(data["EngLearn" + year],232,3,"Eng Learner % " + year,fig)
        plotMap(data["nEngLearn" + year],233,3,"non Eng Learn % " + year,fig)
        plotMap(data["Poverty" + year],235,4,"Poverty % " + year,fig)
        plotMap(data["nPoverty" + year],236,4,"non Poverty % " + year,fig)
        ax      = fig.add_subplot(234)
        ax.text(0, 6, r'The darker the color the higher the number!', fontsize=8)
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])
        ax.axis([0, 10, 0, 10])
        plt.savefig(name,dpi=200) #save them instead of showing cause its a lot

 #plt.show()
        figNum = figNum+1
        
def lrPlots():
#plotting linear regression plots
#beware this makes a lot of graphs
    figu = 1
    for year in years:
        names = ["Total Enroll " + year,"English Learners " + year,"non English Learners " + year,"Poverty " + year,"non Poverty " + year]
        dataFrame = pd.DataFrame({names[0]: pd.Series(data["TotalEnroll" + year]),
                                  names[1]: pd.Series(data["EngLearn#" + year]),
                                  names[2]: pd.Series(data["nEngLearn#" + year]),
                                  names[3]: pd.Series(data["Poverty#" + year]),
                                  names[4]: pd.Series(data["nPoverty#" + year])
                                  })
        for name in names:
            for n in names:
                if(name != n):
                    plt.figure(figu)
                    plt.suptitle(name + " vs " + n) 
                    sns.regplot(x=name, y=n, data=dataFrame,color="b")
                    plt.savefig(name + " vs " + n,dpi=200) #save them instead of showing cause its a lot
                    figu+=1
                                  
    
def main():
    lrPlots()
    mapPlots()
main()
    
