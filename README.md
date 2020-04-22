# NLP-4-SEO-Experiment
This project experiments with the Google NLP Algorithm to evaluate e-commerce product titles and descriptions from an SEO perspective. The first step are scripts that collect the data located in the **data-mining** folder. Next is analysis in the **data-analysis** folder (to be added). Finally a predictive model is in the **data-learning** folder (to be added). To try this, you need a website in Google Search Console and a Google Clound Platform account to enable the Google Search Console API and NLP API. This project uses data from [uselessthingstobuy.com](uselessthingstobuy.com).

## Data Mining
This folder contains scripts that access, clean and export data in csv files located in the **datasets** folder.

**1_traffic-by-query.py** - This accesses the Google Search Console API and collects the page, query, and search data. It requires installing and authorizing the API plus a client_secret.json file. I put this file in with the secret removed. Information on getting started can be found here: [Python Search Console Quickstart](https://developers.google.com/webmaster-tools/search-console-api-original/v3/quickstart/quickstart-python). This script exports file **traffic_by_query.csv**. 

**2_descriptions-data.py** - This is a webscraper that grabs the **traffic_by_query.csv** file and scrapes all of the URLS. It first checks that the URLS do not produce any error codes. Then, it scrapes for the titles and descriptions. Next, it cleans the text data by performing *stemming*. I figured out that without removing stemming, the Google NLP algorithm will return duplicate entities for one text. So, I am not positive this part is necessary, but it works for experimental purposes. 

**3_entity_and_salience.py** - This file accesses the Google NLP API and returns the entities and corresponding salience scores for each title and description. It requires an API key which you can figure out here: [Google NLP API QuickStart](https://cloud.google.com/natural-language/docs/quickstart). It requires a key.json file. I included one here so you can see the setup, but you need to produce your own secret key.

**URL_dates.csv** - This file is downloaded from Wordpress and cleand in excel. It includes the dates each page was published, which is imported in the descriptions-data.py file. 

## Data Analysis
Analysis of our variables. Work in progress.

## Learning Model
Learning model. Work in progress
