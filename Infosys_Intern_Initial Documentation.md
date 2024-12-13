**Understanding of the Problem Statement:**

Supply chain disruptions, caused by factors like global events, demand fluctuations, and logistical challenges, lead to inventory imbalances, increased costs, and lost revenue. An AI-driven system is needed to predict disruptions and optimize inventory management to mitigate these risks and ensure operational continuity.

- AI-driven system to predict supply chain disruptions and optimize inventory levels.  
- Integrates global supply chain data, using NLP and machine learning for disruption prediction and inventory management.  
- Real-time notifications and Inventory Adjustment Module   
- Project focuses on proactive management of supply chain disruptions and efficient inventory optimization, thereby reducing losses and improving operational efficiency.

1. **Objective**: Monitor and analyze global supply chain data sources, such as news articles, supplier information, and transportation updates, to identify emerging disruptions.  
2. **Approach**: NLP is used to process textual data from external sources to extract meaningful insights about disruptions.  
3. **Implementation**: The Event Registry API is utilized to extract relevant articles, focusing on keywords like “supply chain disruption.”  
4. **Data Extraction**: Articles are fetched by making a GET request to the Event Registry API using an API key. The results are saved in a CSV file for further processing.  
5. **Summarization**: TextRank algorithm, implemented using the Sumy library, is applied to summarize article content to extract key details related to disruptions.  
6. **Disruption Type Classification**: A basic keyword-based approach identifies disruption types (e.g., "logistics," "production delay," "inventory shortage") based on article content.

### **Setup and Initial Implementation:**

1. **API Integration**: Event Registry API key is configured to fetch news articles related to supply chain disruptions.  
2. **Data Preprocessing**: Articles are retrieved based on the query parameters, such as keywords, date range, and language. The data is then cleaned and saved in a CSV format for further analysis.  
3. **Summarization**: The TextRank summarizer condenses long content into a few key sentences, providing an easily digestible summary of each article.  
4. **Disruption Type Identification**: The content of each article is analyzed for keywords, which are used to classify disruptions into categories.  
5. **Output**: The summarized content and disruption type for each article are stored in a new CSV file, making it ready for further analysis or use in predictive models.

