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
                """
                data["TotalEnroll" + year].append(int(row['Total Enrollment']))
                data["EngLearn" + year].append(int(row['# English Language Learners']))
                data["nEngLearn" + year].append(int(row['Total Enrollment']) - int(row['# English Language Learners']))
                data["Poverty" + year].append(int(row['# Poverty']))
                data["nPoverty" + year].append(int(row['Total Enrollment']) - int(row['# Poverty']))
                """
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
def plotMap(list,plot,color,title):
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
 
#mapping 5 graphs in a look 
figNum = 1
for year in years:
    fig = plt.figure(figNum)
    plt.suptitle(year+ " NYC School District Change Poverty and English Learners")
    plotMap(data["TotalEnroll"+year],231,0,"Total Enroll "+year)
    plotMap(data["EngLearn" + year],232,3,"Eng Learner % " + year)
    plotMap(data["nEngLearn" + year],233,3,"non Eng Learn % " + year)
    plotMap(data["Poverty" + year],234,4,"Poverty % " + year)
    plotMap(data["nPoverty" + year],235,4,"non Poverty % " + year)
    plt.show()
    figNum = figNum+1
