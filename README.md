<div style="text-align:left">
<div style="text-align:center;display:block"><font face="georgia, serif" size="6">
<div>
<div><span style="background-color:transparent">
<div><span style="background-color:transparent">
<div><span style="background-color:transparent">
<div><span style="background-color:transparent"><font size="25">Migration of Language and Income in NY</font></span></div>
</span></div>
</span></div>
</span></div>
</div>
</font></div>
<div style="text-align:center;display:block"><font size="1">by Josue Rojas</font></div>
<div style="text-align:center;display:block"><font size="1">Github -&nbsp;<a href="https://goo.gl/QrgTbd" target="_blank">https://goo.gl/QrgTbd</a></font></div>
<div style="text-align:center;display:block"><br>
</div>
<div style="text-align:center;display:block"><br>
</div>
<div style="text-align:center;display:block"><br>
</div>
<div style="text-align:left;display:block"><b><font size="3">Question: Is there a relationship between migration vs language vs income?</font></b></div>
<div style="text-align:left;display:block">Migration Patterns are very complex to be define with a few parameters. I do not wish to define why people migrate but to see if there is a correlation between these factor also showing their exist the idea of self segregation where people move around and sort themselves to be with people that share similar characteristics. My theory is that there doe exist this correlation and self-segragation can be seen by plotting it. First I would investigate if there is a relationship between income and the language you speak in NY. It almost seems empirical that in a country (US) where the major language is english, the most high income jobs should go to one of these english speakers. But there is the moment where english might be fading and being overshadowed by other languages such as spanish, especially for some popular migrant destinations such as California (L.A). I will try to clear some of these theories by using linear regression to compare languages with each other and languages and their average income using census data from 2005 - 2014. I will also use school data&nbsp;<span style="background-color:transparent">and</span><span style="background-color:transparent">&nbsp;basemap&nbsp;</span><span style="background-color:transparent">to show</span><span style="background-color:transparent">&nbsp;a map of NYC and the changes of heavy populated non english speakers through 2011 - 2015 and another map to show changes of heavy population of people on the poverty line. Hopefully this will help understand the relationship of language, income, and migration in NY and show visually movement in a self-segregation method.&nbsp;</span></div>
<div style="text-align:left;display:block"><span style="background-color:transparent"><br>
</span></div>
<div style="text-align:left;display:block"><b><font size="3">Data:</font></b></div>
<div style="text-align:left;display:block">For this project I used data from the Census, Public School, and District Maps</div>
<div style="text-align:left;display:block"><a href="https://goo.gl/PnajC3">Census PUMs Data&nbsp;2005 - 2014</a></div>
<div style="text-align:left;display:block"><span style="background-color:transparent">-&nbsp;For this data set you need a </span><a href="http://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2010-2014.pdf" target="_blank">dictionary</a><span style="background-color:transparent"> to understand it. I pulled household language and household financial income.&nbsp;</span></div>
<div style="text-align:left;display:block"><a href="http://goo.gl/jJ5Yj8" target="_blank">Public School Annual Enrollment</a></div>
<div style="text-align:left;display:block"><span><span><span>-&nbsp;</span></span>This was divided nicely into districts that can be easily mapped with my other source. I also used this to show a relationship between income and english learner.&nbsp;</span><br>
</div>
<div style="text-align:left;display:block"><a href="https://goo.gl/RTnFCk" target="_blank">School District Maps</a></div>
<div style="text-align:left;display:block"><span>- This was used with matplotlib to show relationship of student who are &nbsp;english learners and are in the poverty line.</span><br>
</div>
<div style="text-align:left;display:block"><span><br>
</span></div>
<div style="text-align:left;display:block"><span><b>Techniques &amp; Results:</b></span></div>
<div style="text-align:left;display:block"><span style="background-color:transparent">For the census data&nbsp;</span><span style="background-color:transparent">I used seaborn and matplotlib to plot the data. </span><span style="background-color:transparent">I used linear regression between languages vs each other, and vs the total of all people. The blue chart is total of people vs english speakers. The green one is spanish speakers vs total of people. Finally the red one is english speakers vs spanish speakers. These plots show that&nbsp;there is a positive relationship between total of people and the number of spanish speakers in NY. As for english the relationship it has a negative slope.&nbsp;</span></div>
<div style="text-align:left;display:block">
<div style="display:block;text-align:center;margin-right:auto;margin-left:auto"><a href="https://sites.google.com/site/josuerojasportfolio/python/migration-of-language-and-income/LR_Languge_VS_Each_Other.png?attredirects=0" imageanchor="1"><img border="0" height="229" src="https://sites.google.com/site/josuerojasportfolio/python/migration-of-language-and-income/LR_Languge_VS_Each_Other.png" width="400"></a></div>
<br>
</div>
<div style="text-align:left;display:block">I then used linear regression between average income for their respective language. The blue chart is total of people vs their average income. It has a positive slope meaning as the amount of people increases so does their average income. The green chart is total spanish speakers vs their average income. Again similar to the blue chart it has a positive relation, where if total spanish speakers increases so does their average income. The red chart is english speakers and their average income. This chart shows a straight line which means their is no relationship between english speakers and their average income.&nbsp;</div>
<div style="text-align:left;display:block">
<div style="display:block;text-align:center;margin-right:auto;margin-left:auto"><a href="https://sites.google.com/site/josuerojasportfolio/python/migration-of-language-and-income/LR_Language_Income.png?attredirects=0" imageanchor="1"><img border="0" height="227" src="https://sites.google.com/site/josuerojasportfolio/python/migration-of-language-and-income/LR_Language_Income.png" width="400"></a></div>
<br>
</div>
<div style="text-align:left;display:block"><br>
</div>
<div style="text-align:left;display:block">For the school data I used both linear regression and basemap to plot the data. For linear regression I decided to overdo it and compare all possible combinations of people in the poverty, in the non poverty, english learners, non english learners, total enrollment. To show all this I made a web app to let users see the plots.
</div>
<div style="text-align:left;display:block"><span><b>
<center><br>
</center>
<center>
<div><img src="https://www.google.com/chart?chc=sites&amp;cht=d&amp;chdp=sites&amp;chl=%5B%5BGoogle+Apps+Script'%3D20'f%5Cv'a%5C%3D0'10'%3D499'0'dim'%5Cbox1'b%5CF6F6F6'fC%5CF6F6F6'eC%5C0'sk'%5C%5B%22plots%22'%5D'a%5CV%5C%3D12'f%5C%5DV%5Cta%5C%3D10'%3D0'%3D500'%3D547'dim'%5C%3D10'%3D10'%3D500'%3D547'vdim'%5Cbox1'b%5Cva%5CF6F6F6'fC%5CC8C8C8'eC%5C'a%5C%5Do%5CLauto'f%5C&amp;sig=r6XMGGk-cEYIuzOE6eSz3rL9xUE" data-origsrc="https://script.google.com/macros/s/AKfycbwu6nf1gKjDICvNy54Mr3nd0RDbb29cA1mFnmO0RF1cE6OHBno/exec" data-type="maestro" data-props="align:center;borderTitle:plots;height:550;showBorder:false;showBorderTitle:false;wrap:false;" width="500" height="550" style="display:block;margin:5px auto;text-align:center;">
<div></div>
</div>
<div><font color="#999999" size="1">(if you cannot see the script then &nbsp;you must log in to google)</font></div>
<br>
</center>
</b></span></div>
<div style="text-align:left;display:block"><span>
<div>
<div>
<div>For this data set I used basemap to map the districts showing highest numbers as a darker color compare to smaller for # poverty, # non poverty, # english learners, # non english learners, and total enrollments for years 2011-2016. This is where I planned to show the migration or movements of language and their change income. Although you can see tiny changes in all charts in some parts of the boroughs, it does not have enough data information such as previous locations to show a more dramatic change. (ignore staten island since there exist only one district which will always be the same)</div>
<div>
<center>
<div style="max-width:500px">
  <img src="https://media.giphy.com/media/l396NDVhzo2UvGAX6/giphy.gif" style="width:100%;display:block;margin-right:auto;margin-left:auto;text-align:center">
</div>
</center>
<div><br>
</div>
<br>
</div>
<br>
</div>
<br>
</div>
<br>
</span></div>
<div style="text-align:left;display:block"><b>Citation&nbsp;</b></div>
<div style="text-align:left;display:block">Data</div>
<div style="text-align:left;display:block">
<ul><li>Census PUMs</li>
<ul><li>Data used was from 2005 - 2014</li>
<ul><li><a href="https://www.census.gov/programs-surveys/acs/data/pums.html">https://www.census.gov/programs-surveys/acs/data/pums.html</a> ('Housing Unit Record')&nbsp;</li></ul>
<li>You need a dictionary to decipher the csv files.&nbsp;</li>
<ul><li><a href="http://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2010-2014.pdf">http://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2010-2014.pdf</a></li></ul></ul>
<li>Public School Data</li>
<ul><li><a href="http://schools.nyc.gov/NR/rdonlyres/20056B95-8351-4E45-B8A1-9901B4B6A93B/0/DemographicSnapshot201112to201516Public_FINAL.xlsx">http://schools.nyc.gov/NR/rdonlyres/20056B95-8351-4E45-B8A1-9901B4B6A93B/0/DemographicSnapshot201112to201516Public_FINAL.xlsx</a></li></ul>
<li>NYC District maps</li>
<ul><li><a href="https://data.cityofnewyork.us/Education/School-Districts/r8nu-ymqj">https://data.cityofnewyork.us/Education/School-Districts/r8nu-ymqj</a></li></ul></ul>
</div>
<div style="text-align:left;display:block">Source Code Python</div>
<div style="text-align:left;display:block">
<ul><li><span style="background-color:transparent">For Census data plots</span></li>
<ul><li><span style="background-color:transparent"><a href="https://github.com/josuerojasrojas/Migration_of_Language_and_Income/blob/master/censusPlots.py">https://github.com/josuerojasrojas/Migration_of_Language_and_Income/blob/master/censusPlots.py</a></span></li></ul>
<li>For public school&nbsp;</li>
<ul><li><a href="https://github.com/josuerojasrojas/Migration_of_Language_and_Income/blob/master/schoolPlot.py">https://github.com/josuerojasrojas/Migration_of_Language_and_Income/blob/master/schoolPlot.py</a></li></ul>
<li>Images From plots</li>
<ul><li>From Census</li>
<li>From School&nbsp;</li>
<ul><li>All linear regression plots</li>
<ul><li><a href="https://github.com/josuerojasrojas/Migration_of_Language_and_Income/tree/master/Images/schoolf">https://github.com/josuerojasrojas/Migration_of_Language_and_Income/tree/master/Images/schoolf&nbsp;</a></li></ul>
<li>Maps (this also contains plots from linear regression which i need to delete cause they are duplicates)</li>
<ul><li><a href="https://github.com/josuerojasrojas/Migration_of_Language_and_Income/tree/master/Images/school">https://github.com/josuerojasrojas/Migration_of_Language_and_Income/tree/master/Images/school</a></li></ul></ul></ul></ul>
</div>
</div>
