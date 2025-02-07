# Risk Factorization:
- Textual Risk: Sentiment analysis of the Summary column determines whether the text reflects a negative or positive sentiment. Negative sentiment contributes more to the risk factor.
- Computed Risk Factor: Combines the normalized numerical columns (Inventory Level, Lead Time, etc.) with the textual risk for a holistic risk factor.
- Risk Labels: Categorizes risk into High, Medium, or Low based on the computed risk factor.
  
# Summarization:
- Vectorization: Converts numerical columns into a format suitable for querying.
- Query-Based Insights: Dynamically calculates metrics like average, maximum, and minimum values for the numerical columns.

## Outputs - Hugging Face Models:
- Risk Factorization:
  - Dataset saved as risk_factorized_data.csv with additional columns:
    - Output data path: https://docs.google.com/spreadsheets/d/1cDmNxprx0npX_smye_oS6JyPX_7B18d_PJe_x8vv7x8/edit?usp=sharing
    1. Textual Risk
    2. Computed Risk Factor
    3. Risk Label (High, Medium, Low)
- Summarization:
  - On running example queries:
    1. Average Risk Factor: Returns the mean risk factor value.
    2. Maximum Inventory Level: Returns the highest inventory level.
    3. Minimum Lead Time: Returns the shortest lead time.
- Risk Factor Ranges:
  - The Computed Risk Factor is calculated using a weighted combination of:
    1. Textual Risk (based on sentiment analysis of summaries).
    2. Inventory Level (normalized numerical column).
    3. Lead Time (days) (normalized numerical column).
    4. News Sentiment (normalized numerical column).
  - High Risk: Computed Risk Factor >= 0.6
  - Medium Risk: 0.3 <= Computed Risk Factor < 0.6
  - Low Risk: Computed Risk Factor < 0.3

- High-risk entities indicate significant potential for disruptions or delays.
- Medium-risk entities suggest moderate concerns requiring monitoring.
- Low-risk entities are stable and less likely to face disruptions.

## Using Roberta & BART:
- Risk Factorization:
  - Model Used: roberta-base is used for sequence classification.
- Risk Calculation:
  - LABEL_0: Indicates a lower risk sentiment.
  - LABEL_1: Indicates a higher risk sentiment.
  - Risk is calculated as a weighted combination of the scores.
- Output:
  - A normalized risk factor (Risk Factor) and corresponding Risk Label (High, Medium, Low).
  - Summarization:
    - Model Used: facebook/bart-large-cnn, a transformer-based summarization model.
    - Dynamic Query Support: Users can input any query, and the summarization model generates insights.
    - Outputs:
      1. Risk Factorized Data: File saved with calculated risk factors and labels.
      2. Summarized Data: Summaries of the Summary column.
      3. Aggregated Results: Region- and supplier-wise aggregation of risks, inventory levels, and sentiments.

