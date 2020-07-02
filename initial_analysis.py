#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:31:58 2020

@author: margaretsant
"""

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns
from itertools import cycle, islice
from scipy import stats
import statistics
#%%
page_traffic = pd.read_csv("traffic_by_page.csv")
page_traffic = page_traffic.drop(['Unnamed: 0'], axis=1)
page_traffic['URL'] = page_traffic['URL'].str.strip('[]')

query_traffic = pd.read_csv("traffic_by_query.csv")
query_traffic = query_traffic.drop(['Unnamed: 0'], axis=1)
#%%

#####   Initial Exploration of the Data
#%% Statisical Info
page_traffic.info()
page_traffic.head()
page_traffic.describe()

query_traffic.info()
query_traffic.head()
query_traffic.describe()
#%%
##  Page Clicks Distribution:
#%%
#   Histogram:
plt.figure(figsize=(6, 4))
plt.title("Distribution of Page Clicks")
sns.distplot(page_traffic.Clicks,bins=200)

#%%
#   Normal Distribution
sns.set()
mu, sigma = statistics.mean(page_traffic.Clicks), statistics.stdev(page_traffic.Clicks)
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.title("Normal Distribution of Page Clicks")
plt.show()

#%%
##  Page Impressions Distribution:
#%%
#   Histogram
plt.figure(figsize=(16, 8))
plt.title("Distribution of Page Impressions")
sns.distplot(page_traffic.Impressions,bins=200)
#%%
#   Normal Distribution
sns.set()
mu, sigma = statistics.mean(page_traffic.Impressions), statistics.stdev(page_traffic.Impressions)
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.title("Normal Distribution of Page Impressions")
plt.show()

#%%
##  Page CTR Distribution:
#%%
#   Histogram
plt.figure(figsize=(16, 8))
plt.title("Distribution of Page CTR")
sns.distplot(page_traffic.CTR,bins=200)
#%%
#   Normal Distribution
sns.set()
mu, sigma = statistics.mean(page_traffic.CTR), statistics.stdev(page_traffic.CTR)
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.title("Normal Distribution of Page CTR")
plt.show()
#%%
##  Page Position Distribution:
#%%
#   Histogram
plt.figure(figsize=(16, 8))
plt.title("Distribution of Page Position")
sns.distplot(page_traffic.Position,bins=100)
#%%
#   Normal Distribution
sns.set()
mu, sigma = statistics.mean(page_traffic.Position), statistics.stdev(page_traffic.Position)
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.title("Normal Distribution of Page Position")
plt.show()
#%%
##  Query Clicks Distribution:
#%%
#   Histogram
plt.figure(figsize=(16, 8))
plt.title("Distribution of Query Clicks")
sns.distplot(query_traffic.Clicks,bins=200)
#%%
#   Normal Distribution
sns.set()
mu, sigma = statistics.mean(query_traffic.Clicks), statistics.stdev(query_traffic.Clicks)
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.title("Normal Distribution of Query Clicks")
plt.show()
#%%
##  Query Impressions Distribution:
#%%
#   Histogram
plt.figure(figsize=(16, 8))
plt.title("Distribution of Query Impressions")
sns.distplot(query_traffic.Impressions,bins=200)
#%%
#   Normal Distribution
sns.set()
mu, sigma = statistics.mean(query_traffic.Impressions), statistics.stdev(query_traffic.Impressions)
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.title("Normal Distribution of Query Impressions")
plt.show()
#%%
##  Query CTRs Distribution:
#%%
#   Histogram
plt.figure(figsize=(16, 8))
plt.title("Distribution of Query CTR")
sns.distplot(query_traffic.CTR,bins=200)
#%%
#   Normal Distribution
sns.set()
mu, sigma = statistics.mean(query_traffic.CTR), statistics.stdev(query_traffic.CTR)
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.title("Normal Distribution of Query CTR")
plt.show()
#%%
##  Query Positions Distribution:
#%%
#   Histogram
plt.figure(figsize=(16, 8))
plt.title("Distribution of Query Position")
sns.distplot(query_traffic.Position,bins=200)
#%%
#   Normal Distribution
sns.set()
mu, sigma = statistics.mean(query_traffic.Position), statistics.stdev(query_traffic.Position)
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.title("Normal Distribution of Query Position")
plt.show()
#%%
#   Correlation Heat Maps
#%%
#   Correlation Matrix Page Traffic
plt.figure(figsize=(16, 8))
plt.title("Correlation Heat Map for Page Traffic")
sns.set(style="whitegrid")
corr = page_traffic.corr()
sns.heatmap(corr,annot=True,cmap="coolwarm")

#   Correlation Matrix Query Traffic
plt.figure(figsize=(16, 8))
plt.title("Correlation Heat Map for Query Traffic")
sns.set(style="whitegrid")
corr = query_traffic.corr()
sns.heatmap(corr,annot=True,cmap="coolwarm")
#%%
###   Labeled Histograms
#%%
#   Clicks
page_traffic['Product'] = page_traffic['URL'].str.split('/product/')
page_traffic['Product'] = page_traffic['Product'].apply(lambda x: x[1])


color = cm.hsv(np.linspace(.4, .8, 30))
figure,axarr = plt.subplots(1,2, figsize=(20, 40))
df1 = page_traffic.groupby("Product")["Clicks"].mean().sort_values(ascending=False).head(60)
df2 = query_traffic.groupby("Query")["Clicks"].mean().sort_values(ascending=False).head(60)
p1 = df1.plot(kind='barh',ax=axarr[0], color = color)
p1.invert_yaxis()
axarr[0].set_title('Top Pages by Clicks')
axarr[0].set_ylabel('', visible=False)
axarr[0].set_xlabel('Clicks', fontsize=6)
axarr[0].tick_params(labelrotation=20,labelsize=6)
axarr[0].invert_xaxis
p2 = df2.plot(kind='barh',ax=axarr[1],  color = color)
p2.invert_yaxis()
axarr[1].set_title('Top Queries by Clicks')
axarr[1].set_ylabel('', visible=False)
axarr[1].set_xlabel('Clicks', fontsize=6)
axarr[1].tick_params(labelrotation=20,labelsize=6)
figure.tight_layout()
plt.show()

#%%
#   Impressions

figure,axarr = plt.subplots(1,2, figsize=(16, 8))
df1 = page_traffic.groupby("Product")["Impressions"].mean().sort_values(ascending=False).head(60)
df2 = query_traffic.groupby("Query")["Impressions"].mean().sort_values(ascending=False).head(60)
p1 = df1.plot(kind='barh',ax=axarr[0], color = color)
p1.invert_yaxis()
axarr[0].set_title('Top Pages by Impressions')
axarr[0].set_ylabel('', visible=False)
axarr[0].set_xlabel('Impressions', fontsize=6)
axarr[0].tick_params(labelrotation=20, labelsize=6)
p2 = df2.plot(kind='barh',ax=axarr[1],  color = color)
p2.invert_yaxis()
axarr[1].set_title('Top Queries by Impressions')
axarr[1].set_ylabel('', visible=False)
axarr[1].set_xlabel('Impressions', fontsize=1)
axarr[1].tick_params(labelrotation=20, labelsize=6)
figure.tight_layout()
plt.show()

#%%
# CTR

figure,axarr = plt.subplots(1,2, figsize=(16, 8))
df1 = page_traffic.groupby("Product")["CTR"].mean().sort_values(ascending=False).head(60)
df2 = query_traffic.groupby("Query")["CTR"].mean().sort_values(ascending=False).head(60)
p1 = df1.plot(kind='barh',ax=axarr[0], color = color)
p1.invert_yaxis()
axarr[0].set_title('Top Pages by Click-Through-Rate (CTR)')
axarr[0].set_ylabel('', visible=False)
axarr[0].set_xlabel('CTR', fontsize=6)
axarr[0].tick_params(labelrotation=20, labelsize=6)
p2 = df2.plot(kind='barh',ax=axarr[1],  color = color)
p2.invert_yaxis()
axarr[1].set_title('Top Queries by Average Click-Through-Rate (CTR)')
axarr[1].set_ylabel('', visible=False)
axarr[1].set_xlabel('CTR', fontsize=6)
axarr[1].tick_params(labelrotation=20, labelsize=6)
figure.tight_layout()
plt.show()

#%%
# Positions

figure,axarr = plt.subplots(1,2, figsize=(16, 8))
df1 = page_traffic.groupby("Product")["Position"].mean().sort_values(ascending=True).head(60)
df2 = query_traffic.groupby("Query")["Position"].mean().sort_values(ascending=True).head(60)
p1 = df1.plot(kind='barh',ax=axarr[0], color = color)
p1.invert_yaxis()
axarr[0].set_title('Top Pages by Average Position')
axarr[0].set_ylabel('', visible=False)
axarr[0].set_xlabel('Position', fontsize=6)
axarr[0].tick_params(labelrotation=20, labelsize=6)
p2 = df2.plot(kind='barh',ax=axarr[1],  color = color)
p2.invert_yaxis()
axarr[1].set_title('Top Queries by Average Position')
axarr[1].set_ylabel('', visible=False)
axarr[1].set_xlabel('Position', fontsize=6)
axarr[1].tick_params(labelrotation=20, labelsize=6)
figure.tight_layout()
plt.show()

#%%
###     Number of Queries Per URL  
#%%
#   Counting the Number of Queries per URL
# x = query_traffic[query_traffic.URL == page_traffic.URL[0]].Query
Number_queries = []
queries_by_url = []

for i in range(len(page_traffic)):
    queries = []
    for j in range(len(query_traffic)):
        if query_traffic.URL[j]==page_traffic.URL[i]:
            queries.append(query_traffic.Query[j])
    Number_queries.append(len(queries))
    queries_by_url.append(queries)
    #print(queries)
    
page_traffic["Number_of_Queries"] = Number_queries

#%%
##   Scatter Plots for Queries per top URLS
#%%
#   Number of Queries v Clicks / Impressions
figure,axarr = plt.subplots(2,1, figsize=(16, 8))
page_traffic.plot(kind='scatter',x = "Number_of_Queries",y = "Clicks", ax=axarr[0], title='Number of Queries effect on Clicks and Impressions')
axarr[0].text(178,3322, 'toblerone-extra-large-jumbo-4-5-kg-toblerone-bar/', horizontalalignment='right', verticalalignment="top", fontsize=8)
axarr[0].text(26,3255, 'canned-unicorn-meat/', horizontalalignment='right', fontsize=8)
axarr[0].text(36,1510, 'give-nothing-for-the-person-who-has-everything', horizontalalignment='right', fontsize=8)
axarr[0].text(20,823, 'screaming-goat-toy/', horizontalalignment='right', fontsize=8)
axarr[0].text(83,21, '4-sets-of-lightsaber-glowing-chopsticks/', horizontalalignment='left', verticalalignment='bottom', fontsize=8)
axarr[0].text(21,601, 'joke-hand-sanitizer/', horizontalalignment='right', fontsize=8)
axarr[0].text(26,544, 'dick-trophy/', horizontalalignment='left', fontsize=8)
axarr[0].text(63,16, '12-month-membership-to-the-peanut-butter-jelly-month-club/', horizontalalignment='left', verticalalignment='top',fontsize=8)
page_traffic.plot(kind='scatter',x = "Number_of_Queries",y = "Impressions", ax=axarr[1])
axarr[1].text(178,213000.0, 'toblerone-extra-large-jumbo-4-5-kg-toblerone-bar/', horizontalalignment='right', verticalalignment="top",fontsize=8)
axarr[1].text(26,50596.0, 'canned-unicorn-meat/', horizontalalignment='right', fontsize=8)
axarr[1].text(36,42666.0, 'give-nothing-for-the-person-who-has-everything', horizontalalignment='left', fontsize=8)
axarr[1].text(20,36088.0, 'screaming-goat-toy/', horizontalalignment='right',verticalalignment = "top", fontsize=8)
axarr[1].text(83,2602.0, '4-sets-of-lightsaber-glowing-chopsticks/', horizontalalignment='right', fontsize=8)
plt.show()
#%%
#   Correlation heat map with no. of queries 

plt.figure(figsize=(16, 8))
plt.title("Correlation Heat Map for Page Traffic")
sns.set(style="whitegrid")
corr = page_traffic.corr()
sns.heatmap(corr,annot=True,cmap="coolwarm")

#%%
#   Distribution of Number of Queries Plots:

# Number of Queries
plt.figure(figsize=(16, 8))
sns.distplot(page_traffic.Number_of_Queries,bins=100)
plt.xlim(1,178)
#%%
#    Donut Chart for Query Breakdown: Toblerone v. Unicorn Meat
#%%
# filter query data by Toblerone product
is_toblerone_product = query_traffic['URL'] == "'https://www.uselessthingstobuy.com/product/toblerone-extra-large-jumbo-4-5-kg-toblerone-bar/'"
toblerone_product = query_traffic[is_toblerone_product]

def my_autopct(pct):
    return ('%.2f%%' % pct) if pct > 1.5 else ''
#%%
#   Toblerone Clicks donut plot
plt.title("Giant Toblerone Page Clicks divided by Queries")
plt.pie(toblerone_product.Clicks,
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = toblerone_product[toblerone_product.Clicks>50].Query,
           fontsize= 6, 
           title="Top Queries\n(over 50 Clicks)", 
           title_fontsize=10,
           loc="lower right")
plt.show()
#%%
#   Toblerone Impressions Donut Plot
plt.title("Giant Toblerone Page Impressions by Queries")
plt.pie(toblerone_product.Impressions.sort_values(ascending=False),
        colors = color,
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = toblerone_product[toblerone_product.Impressions>2000].Query, 
           fontsize= 6, 
           title="Top Queries\n(over 2000 Impressions)", 
           title_fontsize=10,
           loc="lower right")
plt.show()
#%%
# filter query data by unicorn meat product
is_unicornmeat_product = query_traffic['URL'] == "'https://www.uselessthingstobuy.com/product/canned-unicorn-meat/'"
unicornmeat_product = query_traffic[is_unicornmeat_product]
#%%
#   Unicorn Meat Clicks donut plot
plt.title("Unicorn Meat Page Clicks divided by Queries")
plt.pie(unicornmeat_product.Clicks,
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = unicornmeat_product[unicornmeat_product.Clicks>50].Query, 
           fontsize= 6,
           title = "Top Queries\n(over 50 Clicks)",
           title_fontsize=10,
           loc="lower left")
plt.show()
#%%
#   Unicorn Meat Impressions donut plot
plt.title("Unicorn Meat Page Impressions divided by Queries")
plt.pie(unicornmeat_product.Impressions.sort_values(ascending=False),
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = unicornmeat_product[unicornmeat_product.Impressions>2000].Query, 
           fontsize= 6, 
           title = "Top Queries\n(over 2000 Impressions)",
           title_fontsize=10,
           loc="lower left")
plt.show()
#%%
#   Other Top Page Query Breakdowns: Nothing Page, Goat Toy, Hand Sanitizer, Dick Trophy
#%%
#   Gift of Nothing Page
is_nothing_product = query_traffic['URL'] == "'https://www.uselessthingstobuy.com/product/give-nothing-for-the-person-who-has-everything/'"
nothing_product = query_traffic[is_nothing_product]
#%%
# Clicks
plt.title("Gift of Nothing Clicks divided by Queries")
plt.pie(nothing_product.Clicks,
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = nothing_product[nothing_product.Clicks>50].Query, 
           fontsize= 6, 
           title = "Top Queries\n(over 50 Clicks)",
           title_fontsize=10,
           loc="right")
plt.show()
#%%
# Impressions
plt.title("Gift of Nothing Impressions divided by Queries")
plt.pie(nothing_product.Impressions.sort_values(ascending=False),
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = nothing_product[nothing_product.Impressions>2000].Query, 
           fontsize= 6, 
           title = "Top Queries\n(over 2000 Impressions)",
           title_fontsize=10,
           loc="right")
plt.show()
#%%
#   Screaming Goat Toy
is_goat_product = query_traffic['URL'] == "'https://www.uselessthingstobuy.com/product/screaming-goat-toy/'"
goat_product = query_traffic[is_goat_product]
#%%
# Clicks
plt.title("Screaming Goat Toy Clicks divided by Queries")
plt.pie(goat_product.Clicks,
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = goat_product[goat_product.Clicks>20].Query, 
           fontsize= 6, 
           title = "Top Queries\n(over 20 Clicks)",
           title_fontsize=10,
           loc="lower left")
plt.show()
#%%
# Impressions
plt.title("Screaming Goat Toy Impressions divided by Queries")
plt.pie(goat_product.Impressions.sort_values(ascending=False),
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = goat_product[goat_product.Impressions>500].Query, 
           fontsize= 6, 
           title = "Top Queries\n(over 500 Impressions)",
           title_fontsize=10,
           loc="lower left")
plt.show()
#%%
#   Hand Sanitizer
is_sanitizer_product = query_traffic['URL'] == "'https://www.uselessthingstobuy.com/product/joke-hand-sanitizer/'"
sanitizer_product = query_traffic[is_sanitizer_product]
#%%
# Clicks
plt.title("Joke Hand Sanitizer Clicks divided by Queries")
plt.pie(sanitizer_product.Clicks,
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = sanitizer_product[sanitizer_product.Clicks>20].Query, 
           fontsize= 6, 
           title = "Top Queries\n(over 20 Clicks)",
           title_fontsize=10,
           loc="right")
plt.show()
#%%
# Impressions
plt.title("Joke Hand Sanitizer Impressions divided by Queries")
plt.pie(sanitizer_product.Impressions.sort_values(ascending=False),
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = sanitizer_product[sanitizer_product.Impressions>500].Query, 
           fontsize= 6, 
           title = "Top Queries\n(over 500 Impressions)",
           title_fontsize=10,
           loc="right")
plt.show()
#%%
#   Dick Trophy
is_trophy_product = query_traffic['URL'] == "'https://www.uselessthingstobuy.com/product/dick-trophy/'"
trophy_product = query_traffic[is_trophy_product]
#%%
# Clicks
plt.title("D*ck Trophy Clicks divided by Queries")
plt.pie(trophy_product.Clicks,
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = trophy_product[trophy_product.Clicks>20].Query, 
           fontsize= 6, 
           title = "Top Queries\n(over 20 Clicks)",
           title_fontsize=10,
           loc="upper right")
plt.show()
#%%
# Impressions
plt.title("D*ck Trophy Impressions divided by Queries")
plt.pie(trophy_product.Impressions.sort_values(ascending=False),
        colors = color, 
        autopct=my_autopct, pctdistance=1.1,
        textprops={'fontsize': 6})
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(labels = trophy_product[trophy_product.Impressions>500].Query, 
           fontsize= 6, 
           title = "Top Queries\n(over 500 Impressions)",
           title_fontsize=10,
           loc="right")
plt.show()
#%%
##########========== Salience Score Analysis ==========##########
#%%
#   import data:
descript_salience = pd.read_csv("description-salience-data.csv")
title_salience = pd.read_csv("title-salience-data.csv")

#   Clean Data
descript_salience = descript_salience.drop(['Unnamed: 0'], axis=1)
title_salience = title_salience.drop(['Unnamed: 0'], axis=1)
#%%
#   Creating Rows for each Description Entity
d_entities = []
d_saliences = []
d_urls = []
d_text = []
for i in range(len(descript_salience)):
    entities = descript_salience.Description_Entity[i].split(",")
    for j in entities:
        url = descript_salience.URL[i]
        d_urls.append(url)
        text = descript_salience.Description[i]
        d_text.append(text)
        j = str(j)
        j = j.strip("[")
        j = j.strip("]")
        j = j.strip(" ")
        d_entities.append(j)
for i in range(len(descript_salience.Description_Salience)):
    saliences = descript_salience.Description_Salience[i].split(",")
    for j in saliences:
        j = str(j)
        j = j.strip("[")
        j = j.strip("]")
        j = j.strip(" ")
        d_saliences.append(j)
 
## Description Salience New Dataframe       
d_salience_data = pd.DataFrame(list(zip(d_entities,d_saliences,d_urls,d_text)),
                               columns=["Entity","Salience","URL","Text"])
d_salience_data.Salience=d_salience_data.Salience.apply(lambda col:pd.to_numeric(col, errors='coerce'))
d_salience_data.URL = d_salience_data.URL.apply(lambda x: "'" + str(x) + "'")
#%%  
#   Creating Rows for each Title Entity     
t_entities = []
t_saliences = []
t_urls = []
t_text = []
for i in range(len(title_salience)):
    entities = title_salience.Title_Entity[i].split(",")
    for j in entities:
        url = title_salience.URL[i]
        t_urls.append(url)
        text = title_salience.Title[i]
        t_text.append(text)
        j = str(j)
        j = j.strip("[")
        j = j.strip("]")
        j = j.strip(" ")
        t_entities.append(j)
for i in range(len(title_salience.Title_Salience)):
    saliences = title_salience.Title_Salience[i].split(",")
    for j in saliences:
        j = str(j)
        j = j.strip("[")
        j = j.strip("]")
        j = j.strip(" ")
        t_saliences.append(j)

# Title Salience New Dataframe:
t_salience_data = pd.DataFrame(list(zip(t_entities,t_saliences,t_urls,t_text)),
                               columns=["Entity","Salience","URL","Text"])
#%%
#   Merging Traffic Data with Salience on URL
#d_salience_data.Salience=d_salience_data.Salience.apply(lambda col:pd.to_numeric(col, errors='coerce'))
d_salience_data.info()
page_traffic.info()
#d_salience_data = page_traffic.merge(d_salience_data, on="URL")
d_salience_query_data = d_salience_data.merge(query_traffic, on="URL")
#%%
d_salience_data.head()
#%%
descript_salience.describe()

title_salience.info()
title_salience.head()
title_salience.describe()
#%%

print(query_traffic[query_traffic.URL == page_traffic.URL[0]].Query)

traffic_dict = page_traffic.set_index('URL').T.to_dict('list')

traffic_dict[4] = {}

traffic_dict = {'Page_URL':page_traffic.URL,'Page_Clicks':page_traffic.Clicks,
                'Page_Impressions':page_traffic.Impressions,'Page_CTR':page_traffic.CTR,
                'Page_Position':page_traffic.Position,
                'Page_Queries':{}}

'Queries':query_traffic[query_traffic.URL == page_traffic.URL].Query,
                                'Query_Clicks':query_traffic[query_traffic.URL == page_traffic.URL].Clicks,
                                'Query_Impressions':query_traffic[query_traffic.URL == page_traffic.URL].Impressions,
                                'Query_CTR':query_traffic[query_traffic.URL == page_traffic.URL].CTR,
                                'Query_Position':query_traffic[query_traffic.URL == page_traffic.URL].Position


x = query_traffic.URL==page_traffic.URL[0]