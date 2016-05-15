import matplotlib.pyplot as plt
import numpy as np
import csv
import re #force to use this since the data is not uniform
import seaborn as sns
import pandas as pd #used for the dataframe


"""
Everything is commented out becuase to avoid time consumption
I took the total of people in the census in ny, speaking spanish, and speaking english
and for each I took the average income for the years 2005 - 2014
"""
"""
#the locations of PUMS data from 2005 - 2014 using "list comprehension"
years = [y for y in range(5,15)]
PUMS = ["PUMS/household/house" + str(year)+ ".csv" for year in years]
"""
"""
getting the data
the dictionary for the csv titles is here (2010-2014) - http://goo.gl/QD7VSW
"""
"""
data = {}
length = []
slength = []
elength = []
meanTotal = []
meanSpan = []
meanEng = []
floatPattern = r"\d+" #actually an intPattern

for fileName, year in zip(PUMS, years):

    year = str(year) #change year to string because..
    HLanguage = "HHL" + year #household language
    HLEnglish = "HHLEnglish" + year #english only
    HLSpanish = "HHLSpanish" + year #spanish only
    FINCP = "FINCP" + year #household income for all
    FSpanish = "FINCPSpanish" + year #for spanish speakers
    FEnglish = "FINCPEnglish" + year #for english speakers
    
    with open(fileName) as file:
        reader = csv.DictReader(file)
        data[HLanguage] = []
        data[HLSpanish] = []
        data[HLEnglish] = []
        data[FINCP] = []
        data[FSpanish] = []
        data[FEnglish] = []
        for row in reader:
            match = False
            #check if a number is given or else it will cause error when converting to int
            if(re.match(floatPattern,row['FINCP']) != None):
                        match = True
                        data[FINCP].append(int(row['FINCP']))
            data[HLanguage].append(row['HHL'])
            if row['HHL'] == '2':
                if(match):
                    data[FSpanish].append(int(row['FINCP']))
                data[HLSpanish].append(row['HHL'])
            elif row['HHL'] == '1':
                if(match):
                    data[FEnglish].append(int(row['FINCP']))
                data[HLEnglish].append(row['HHL'])
        #all the list are ordered in years
        length.append(len(data[HLanguage]))
        slength.append(len(data[HLSpanish]))
        elength.append(len(data[HLEnglish]))
        meanTotal.append(np.mean(np.array(data[FINCP])))
        meanSpan.append(np.mean(np.array(data[FSpanish])))
        meanEng.append(np.mean(np.array(data[FEnglish])))

#print list to be use for faster code
print "total = ", length
print "totalSpan = ", slength
print "totalEng = ", elength
print "meanTotal = ", meanTotal
print "meanSpan = ", meanSpan
print "meanEng = ", meanEng
"""
total =  [78531, 85108, 85461, 85861, 86256, 86937, 93757, 92810, 92085, 92533]
totalSpan =  [7393, 7643, 7612, 7654, 7840, 8075, 8073, 8490, 7938, 8192]
totalEng =  [55145, 54398, 54499, 54567, 55020, 54691, 54460, 54040, 54838, 54909]
meanTotal =  [82872.716904361543, 86541.661596244128, 91694.376004496808, 95007.511134809611, 95805.030095333044, 94136.426332939009, 93271.050975960548, 94901.926477575558, 100746.62700092469, 103257.14724869351]
meanSpan =  [61102.288099467143, 61236.747150259071, 64531.192147324531, 67609.155878701902, 68040.465108284639, 67164.99751161247, 66211.27864496845, 67577.430252902821, 71216.8277935527, 72335.272367770638]
meanEng =  [86068.977854909492, 90162.320343672633, 95791.782531660283, 98706.266912777239, 99207.081851365161, 98384.284849384188, 97129.295312315502, 99209.920418030568, 105176.59000967373, 108193.02600799342]


#xticks
sYears = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
xAxis = [x for x in range(10)]

"""
the data for english spanish and total are all different ranges so we need to 'normalize' it.
i choose to show percentage change instead of the statistic normalize.
"""
def percentChangeList(list):
    beginning = True
    returnList = []
    for current in list:
        if beginning:
            returnList.append(0) #the first value is 0 cause there is no change
            beginning = False
        else:
            returnList.append(((current - previous) / float(previous)) * 100)
        previous = current
    return returnList

#data frames for seaborn use (pd.Series is not neccessary but just in case its there)
dataFrame = pd.DataFrame({"Language Total": pd.Series(total,index=sYears),
                          "Language English": pd.Series(totalEng,index=sYears),
                          "Language Spanish": pd.Series(totalSpan,index=sYears),
                          "Income Mean Total": pd.Series(meanTotal,index=sYears),
                          "Income Mean English": pd.Series(meanEng,index=sYears),
                          "Income Mean Spanish": pd.Series(meanSpan,index=sYears),
                          "Language % Change Total": pd.Series(percentChangeList(total),index=sYears),
                          "Language % Change English": pd.Series(percentChangeList(totalEng),index=sYears),
                          "Language % Change Spanish": pd.Series(percentChangeList(totalSpan),index=sYears),
                          "Income Mean % Change Total": pd.Series(percentChangeList(meanTotal),index=sYears),
                          "Income Mean % Change English": pd.Series(percentChangeList(meanEng),index=sYears),
                          "Income Mean % Change Spanish": pd.Series(percentChangeList(meanSpan),index=sYears)
                          })

sns.set(style="darkgrid", color_codes=True) #make it look nice

#plots for all total, english, and spanish (change from 2005 - 2014)
plt.figure(1)
plt.suptitle("Language % Change Vs Each Other (All Languages,Spanish,English (2005 - 2014))")
plt.subplot(221) #4x4 grid
plt.plot(percentChangeList(total),label="total",color='b') #plot for percent change in total group
plt.plot(percentChangeList(totalSpan),label="english",color='r') #plot for percent change in english group 
plt.plot(percentChangeList(totalEng),label="spanish",color='g') #plot for percent change in spanish group
plt.xticks(xAxis, sYears) #ticks to make it reflect what it represents
plt.legend()
#plot for spanish and english percent change
plt.subplot(222)
plt.plot(percentChangeList(totalEng),label="english",color='r')
plt.plot(percentChangeList(totalSpan),label="spanish",color='g')
plt.xticks(xAxis, sYears) 
plt.legend()
#plot for total and spanish
plt.subplot(223)
plt.plot(percentChangeList(totalSpan),label="spanish",color='g')
plt.plot(percentChangeList(total),label="total",color='b')
plt.xticks(xAxis, sYears) 
plt.legend()
#plot for total and english
plt.subplot(224)
plt.plot(percentChangeList(totalEng),label="total",color='b')
plt.plot(percentChangeList(total),label="english",color='r')
plt.xticks(xAxis, sYears)
plt.legend()
plt.show()


#plots for regression analysis of languages vs language (not percent change)
#change colors
plt.figure(2)
plt.suptitle("Linear Regression of Languages Vs Each Other (2005 - 2014)")
plt.subplot(221)
sns.regplot(x="Language Total", y="Language English", data=dataFrame,color="b")
plt.subplot(222)
sns.regplot(x="Language Total", y="Language Spanish", data=dataFrame,color="g")
plt.subplot(223)
sns.regplot(x="Language English", y="Language Spanish", data=dataFrame,color="r")
plt.show()


#plots for regression analysis of languages vs language (percent change)
plt.figure(3)
plt.suptitle("Linear Regression of % Change of Languages Vs Each Other (2005 - 2014)")
plt.subplot(221)
sns.regplot(x="Language % Change Total", y="Language % Change English", data=dataFrame,color="b")
plt.subplot(222)
sns.regplot(x="Language % Change Total", y="Language % Change Spanish", data=dataFrame,color="g")
plt.subplot(223)
sns.regplot(x="Language % Change English", y="Language % Change Spanish", data=dataFrame,color="r")
plt.show()

#plots for regression analysis of language vs income (not percent change)
plt.figure(4)
plt.suptitle("Linear Regression of Each Languages Vs Mean Income (2005 - 2014)")
plt.subplot(221)
sns.regplot(x="Language Total", y="Income Mean Total", data=dataFrame,color="b")
plt.subplot(222)
sns.regplot(x="Language Spanish", y="Income Mean Spanish", data=dataFrame,color="g")
plt.subplot(223)
sns.regplot(x="Language English", y="Income Mean English", data=dataFrame,color="r")
plt.show()

#plots for regression analysis of language vs income (percent ccange)
plt.figure(5)
plt.suptitle("Linear Regression of % Change of Each Languages Vs Mean Income (2005 - 2014)")
plt.subplot(221)
sns.regplot(x="Language % Change Total", y="Income Mean % Change Total", data=dataFrame,color="b")
plt.subplot(222)
sns.regplot(x="Language % Change Spanish", y="Income Mean % Change Spanish", data=dataFrame,color="g")
plt.subplot(223)
sns.regplot(x="Language % Change English", y="Income Mean % Change Spanish", data=dataFrame,color="r")
plt.show()
