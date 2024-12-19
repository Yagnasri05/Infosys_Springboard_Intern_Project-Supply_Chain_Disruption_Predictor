# -*- coding: utf-8 -*-
"""Final Dataipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wmafdhjV3I97DH_135POtw6qcrcM708g

# Complete Code for Extracting data using News AI API and Merging with Numerical Data
"""

import requests
import pandas as pd
import spacy

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

# Function to extract locations using spaCy NER
def extract_locations(text):
    doc = nlp(text)
    locations = set([ent.text for ent in doc.ents if ent.label_ == 'GPE'])  # GPE = Geopolitical entity (countries, cities)
    return ", ".join(locations) if locations else 'Unknown'

# Initialize an empty list to store all extracted data
all_data = []

# Number of articles per page
articles_per_page = 200
total_articles_to_fetch = 1000

# Iterate through each keyword to fetch articles
for keyword in keywords:
    print(f"Fetching articles for keyword: {keyword}")
    fetched_articles = 0  # Counter for the total number of articles fetched for the keyword

    while fetched_articles < total_articles_to_fetch:
        # Set up the query parameters
        params = {
            "apiKey": api_key,
            "keyword": keyword,
            "count": articles_per_page,
            "offset": fetched_articles,  # Offset for pagination
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
            break

        # Check if articles are in the response
        if 'articles' in data and 'results' in data['articles']:
            articles = data['articles']['results']

            # Loop through each article to extract details
            for article in articles:
                summary = article.get('body', 'No content available')
                location = extract_locations(summary)

                # Append the extracted data to the list
                all_data.append({
                    'Keyword': keyword,
                    'Title': article.get('title', 'No Title'),
                    'Source': article.get('source', {}).get('title', 'No Source'),
                    'URL': article.get('url', 'No URL'),
                    'Summary': summary,
                    'Location': location,
                })

            # Update the fetched articles count
            fetched_articles += len(articles)

            # Stop if we've fetched enough articles
            if fetched_articles >= total_articles_to_fetch:
                break
        else:
            print(f"No more articles found for keyword: {keyword}")
            break

# Convert the list of extracted data to a DataFrame
df = pd.DataFrame(all_data)

# Save the data to a CSV file
df.to_csv('supply_chain_articles_with_entities_and_location.csv', index=False)
print("Data has been saved to 'supply_chain_articles_with_entities_and_location.csv'")


import pandas as pd

# Load textual and numerical data
textual_data_path = '/content/supply_chain_articles_with_entities_and_location (1).csv'
textual_df = pd.read_csv(textual_data_path)

numerical_data_path = '/content/supply_chain_sample_data.csv'
numerical_df = pd.read_csv(numerical_data_path)

# Drop the 'Location' column from the textual dataset
textual_df = textual_df.drop(columns=['Location'], errors='ignore')

# Add a unique ID column to preserve row order for the textual data
textual_df['Unique_ID'] = range(len(textual_df))

# Ensure the numerical dataset has at least 5,000 rows by reusing rows if necessary
# Repeat numerical data until it matches the size of textual data
repeated_numerical_df = pd.concat([numerical_df] * ((len(textual_df) // len(numerical_df)) + 1), ignore_index=True)
repeated_numerical_df = repeated_numerical_df.iloc[:len(textual_df)]  # Trim to match the textual dataset size

# Add a unique ID column to the numerical data for merging
repeated_numerical_df['Unique_ID'] = range(len(repeated_numerical_df))

# Merge the datasets on the 'Unique_ID' column
final_df = pd.merge(textual_df, repeated_numerical_df, on='Unique_ID')

# Drop the 'Unique_ID' column after merging
final_df = final_df.drop(columns=['Unique_ID'])

# Save the final dataset to a CSV file
final_df.to_csv('/content/merged_supply_chain_data.csv', index=False)

print("Merged data has been saved to '/content/merged_supply_chain_data.csv'")
print(f"Final dataset has {len(final_df)} rows and {len(final_df.columns)} columns.")