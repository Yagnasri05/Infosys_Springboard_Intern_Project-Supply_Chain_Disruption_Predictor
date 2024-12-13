# -*- coding: utf-8 -*-
"""Summarization & Classification of Articles.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wmafdhjV3I97DH_135POtw6qcrcM708g

# Summarization & Classification of the Articles using Sumy TextRank
"""

import pandas as pd
import spacy
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import nltk

# Load SpaCy model for text processing
nlp = spacy.load("en_core_web_sm")

# Download NLTK resources
nltk.download('punkt_tab')

def summarize_content_textrank(content, num_sentences=3):
    # Clean and preprocess content (optional)
    content = re.sub(r'\s+', ' ', content).strip()

    # Create a parser for the content
    parser = PlaintextParser.from_string(content, Tokenizer('english'))  # Specify language as 'english'

    # Initialize the TextRank Summarizer
    summarizer = TextRankSummarizer()

    # Generate the summary (number of sentences)
    summary = summarizer(parser.document, num_sentences)

    # Join the summarized sentences to form a final summary
    return ' '.join(str(sentence) for sentence in summary)

# Example: Function to analyze and identify a disruption type based on keywords
def identify_disruption_type(content):
    disruption_keywords = ['supply chain', 'disruption', 'logistics', 'shipping', 'production delay', 'inventory shortage']
    content_lower = content.lower()

    for keyword in disruption_keywords:
        if keyword in content_lower:
            return keyword.capitalize()

    return "General Disruption"  # Default type

# Read the saved CSV file with articles
df = pd.read_csv('supply_chain_articles.csv')

# Prepare lists to store summarized content, disruption type, and other key details
summarized_content = []
disruption_types = []

# Process each article to summarize and identify disruption type
for index, row in df.iterrows():
    content = row['Summary']

    # Get summarized content using TextRank
    summary = summarize_content_textrank(content)
    summarized_content.append(summary)

    # Identify disruption type from the content
    disruption_type = identify_disruption_type(content)
    disruption_types.append(disruption_type)

# Create a new DataFrame with key details
output_df = pd.DataFrame({
    'Title': df['Title'],
    'Source': df['Source'],
    'URL': df['URL'],
    'Summarized Content': summarized_content,
    'Disruption Type': disruption_types
})

# Save the output DataFrame to a new CSV file
output_df.to_csv('/content/drive/MyDrive/supply_chain_article_summary_textrank.csv', index=False)
print("Summary CSV with key details has been saved as 'supply_chain_article_summary_textrank.csv'.")