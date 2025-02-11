# -*- coding: utf-8 -*-
"""Extraction of Articles_Multiple Keyword.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wmafdhjV3I97DH_135POtw6qcrcM708g

# Extraction of Articles using Event registry with multiple keywords & Different columns
"""

import requests
import pandas as pd
import re
import spacy
from sklearn.cluster import KMeans

# Load spaCy's pre-trained NER model
nlp = spacy.load("en_core_web_sm")

# Define your Event Registry API key
api_key = "a6e45a4f-616a-46b2-ab77-e7b54c6435cc"

# Define the base URL for querying the Event Registry API
url = "https://eventregistry.org/api/v1/article/getArticles"

# List of keywords for multi-topic search
keywords = [
    "supply chain disruption",
    "inventory optimization",
    "logistics delay",
    "shipping routes",
    "supply chain risk",
]

# Function to extract meaningful numerical data with context
def extract_contextual_entities(text):
    entities = {}

    # Extract delays (e.g., "5 days late")
    delays = re.findall(r"(\d+)\s+(days?|hours?)", text)
    entities['Delays'] = ", ".join([f"{d[0]} {d[1]}" for d in delays])

    # Extract costs (e.g., "$300 million")
    costs = re.findall(r"\$\d+(?:,\d+)*(?:\.\d+)?\s*(million|billion)?", text)
    entities['Costs'] = ", ".join(costs)

    # Extract quantities (e.g., "200 containers")
    quantities = re.findall(r"(\d+)\s+(containers?|units?|shipments?)", text)
    entities['Quantities'] = ", ".join([f"{q[0]} {q[1]}" for q in quantities])

    return entities

# Function to extract event-specific dates
def extract_event_dates(text):
    dates = re.findall(r"\b(start|end|expected)\s+date[s]?:?\s+(\w+\s\d{1,2},?\s?\d{4})", text, re.IGNORECASE)
    return {term.lower(): date for term, date in dates}

# Function to extract locations using spaCy NER
def extract_locations(text):
    doc = nlp(text)
    locations = set([ent.text for ent in doc.ents if ent.label_ == 'GPE'])  # GPE = Geopolitical entity (countries, cities)
    return ", ".join(locations) if locations else 'Unknown'

# Initialize an empty list to store all extracted data
all_data = []

# Iterate through each keyword to fetch articles
for keyword in keywords:
    print(f"Fetching articles for keyword: {keyword}")

    # Set up the query parameters
    params = {
        "apiKey": api_key,
        "keyword": keyword,
        "count": 50,  # Number of results to retrieve
        "lang": "eng",  # Language of articles (English)
        "sortBy": "date",  # Sort by date (most recent first)
        "startDate": "2023-01-01",  # Start date for events
        "endDate": "2024-12-31",  # End date for events
    }

    # Send GET request to the API
    response = requests.get(url, params=params)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Convert the response to JSON
    else:
        print(f"Error: {response.status_code}")
        data = {}

    # Check if articles are in the response
    if 'articles' in data and 'results' in data['articles']:
        articles = data['articles']['results']

        # Loop through each article to extract details
        for article in articles:
            summary = article.get('body', 'No content available')

            # Extract contextual entities (numerical data)
            contextual_entities = extract_contextual_entities(summary)

            # Extract event-specific dates
            event_dates = extract_event_dates(summary)

            # Extract location information
            location = extract_locations(summary)

            # Append the extracted data to the list
            all_data.append({
                'Keyword': keyword,
                'Title': article.get('title', 'No Title'),
                'Source': article.get('source', {}).get('title', 'No Source'),
                'URL': article.get('url', 'No URL'),
                'Summary': summary,
                'Delays': contextual_entities.get('Delays', 'N/A'),
                'Costs': contextual_entities.get('Costs', 'N/A'),
                'Quantities': contextual_entities.get('Quantities', 'N/A'),
                'Start Date': event_dates.get('start', 'N/A'),
                'End Date': event_dates.get('end', 'N/A'),
                'Location': location,
            })
    else:
        print(f"No articles found for keyword: {keyword}")

# Convert the list of extracted data to a DataFrame
df = pd.DataFrame(all_data)

# Save the data to a CSV file
df.to_csv('supply_chain_articles_with_entities_and_location.csv', index=False)
print("Data has been saved to 'supply_chain_articles_with_entities_and_location.csv'")