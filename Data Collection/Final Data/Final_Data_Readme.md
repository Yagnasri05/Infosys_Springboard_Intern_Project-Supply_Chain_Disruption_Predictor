# Data Extraction Process & Merging 
1. API Details:
   -The Event Registry API is used to fetch news articles based on keywords related to supply chain topics. The API provides access to global news data and can be accessed at https://eventregistry.org.

2. Textual Data Processing:
   - Articles are fetched for keywords like "supply chain disruption" and "logistics delay."
   - Named Entity Recognition (NER) is performed using spaCy to extract locations from article summaries.
   - The processed data is saved as supply_chain_articles_with_entities_and_location.csv.
    
3. Merging:
   - Textual and numerical datasets are merged using a unique identifier.
   - The merged dataset is saved as merged_supply_chain_data.csv.
  
4. Output Files:
   - supply_chain_articles_with_entities_and_location.csv - Contains extracted article data.
   - merged_supply_chain_data.csv - Final merged dataset with textual and numerical data.

5. Link for the Data Files:
   - Textual Data: https://docs.google.com/spreadsheets/d/1PDlgWXj1nrEL8SduHoevCCh5e2T6DUM6pfwoUwxZyt4/edit?usp=sharing
   - Final Merged Data: https://docs.google.com/spreadsheets/d/16IRVyP_rafxEcg7kS5lX5eFoKIZdzhLu4p2xF28_8H0/edit?usp=sharing
