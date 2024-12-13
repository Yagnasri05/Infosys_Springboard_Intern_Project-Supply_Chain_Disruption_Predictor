# Data Collection & Summarization:
- Fetches articles from the Event Registry API using multiple supply chain-related keywords.
- Extracts numerical data (e.g., delays, costs, quantities), event-specific dates, and geopolitical locations using regex and spaCy.
- Summarizes article content using the TextRank algorithm.
- Identifies the disruption type based on predefined keywords.
- Outputs structured data in CSV format for further analysis

Technologies Used:
- spaCy: For Named Entity Recognition (NER) and location extraction.
- sumy: For TextRank summarization.
- Pandas & re: Pattern matching, data manipulation & extraction.
- Event Registry API: For fetching supply chain-related articles.

Code Flow: 
- Keywords are queried via the Event Registry API.
- Relevant articles are retrieved and parsed.
- NLP techniques (regex and spaCy) extract meaningful contextual information.
- Data is saved as a structured CSV file: supply_chain_articles_with_entities_and_location.csv.

Summarization and Classification Module: 
- Summarize article content using the TextRank algorithm.
- Classify the disruption type based on pre-defined keywords.
- Article content is read from the data collection CSV file.
- TextRank generates a concise summary of each article.
- Disruption types (e.g., "Inventory Shortage," "Production Delay") are identified based on the presence of specific keywords.
- The processed data is saved as a new CSV file: supply_chain_article_summary_textrank.csv.
