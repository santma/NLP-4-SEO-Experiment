#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import pandas as pd

client = language.LanguageServiceClient.from_service_account_json("/Users/margaretsant/Desktop/THESIS-PROJECT/data-mining/key.json")

# The text to analyze
text_data = pd.read_csv("datasets/text-and-traffic-data.csv")
titles = text_data["Title"].tolist()
descriptions = text_data["Description"].tolist()

title_entities = []
title_saliences = []
for i in titles:
    document = types.Document(
            content = i,
            type = enums.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(document=document)
    i_entity = []
    i_salience = []
    for e in response.entities:
        entity = e.name
        salience = e.salience
        i_entity.append(entity)
        i_salience.append(salience)
    title_entities.append(i_entity)
    title_saliences.append(i_salience)

descriptions_entities = []
descriptions_saliences = []
for i in descriptions:
    document = types.Document(
            content = i,
            type = enums.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(document=document)
    i_entity = []
    i_salience = []
    for e in response.entities:
        entity = e.name
        salience = e.salience
        i_entity.append(entity)
        i_salience.append(salience)
    descriptions_entities.append(i_entity)
    descriptions_saliences.append(i_salience) 
        
        
entity_salience_data = pd.DataFrame(list(
        zip(titles,
            title_entities, 
            title_saliences, 
            descriptions, 
            descriptions_entities, 
            descriptions_saliences)),
        columns = ['Title',
                   'Title_Entity',
                   'Title_Salience',
                   'Description',
                   'Description_Entity',
                   'Description_Salience'])





